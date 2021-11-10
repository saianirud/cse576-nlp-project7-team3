import argparse
import glob
import json
import os
import pytorch_lightning as pl
import random
import torch

from num2words import num2words
from pytorch_lightning.callbacks import ModelCheckpoint
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from torch.utils.data import DataLoader
from torch.utils.data import Dataset, random_split

from typing import List


def compute_exact_match(predicted_answer, correct_answer) -> bool:
    predicted_answer = predicted_answer.strip().lower()
    correct_answer = correct_answer.strip().lower()
    return predicted_answer == correct_answer


def convert_to_base(num: int, base: int, numerals="0123456789abcdefghijklmnopqrstuvwxyz") -> str:
    return ((num == 0) and numerals[0]) or (
        convert_to_base(num // base, base, numerals).lstrip(numerals[0]) + numerals[num % base])


def convert_to_character(number: str, separator: str, invert_number: bool, max_digits: int) -> str:
    if max_digits > 0:
        signal = None
        if number[0] == '-':
            signal = '-'
            number = number[1:]
        number = (max_digits - len(number)) * '0' + number
        if signal:
            number = signal + number
    if invert_number:
        number = number[::-1]
    return separator.join(number)


def convert_to_10based(number: str, invert_number: bool) -> str:
    signal = None
    if number[0] == '-':
        signal = '-'
        number = number[1:]

    output = []
    for i, digit in enumerate(number[::-1]):
        if i > 0:
            output.append('1' + i * '0')
        output.append(digit)

    if signal:
        output.append(signal)

    # The output is already inverted. If we want it to _not_ be inverted, then we invert it.
    if not invert_number:
        output = output[::-1]

    return ' '.join(output)


def convert_to_10ebased(number: str, split_type: str, invert_number: bool) -> str:
    signal = None
    if number[0] == '-':
        signal = '-'
        number = number[1:]

    output = []
    for i, digit in enumerate(number[::-1]):
        if split_type is None:
            output.append('10e' + str(i))
        elif split_type == 'underscore':
            output.append('10e' + '_'.join(str(i)))
        elif split_type == 'character':
            output.append(' '.join('D' + str(i) + 'E'))
        else:
            raise Exception(f'Wrong split_type: {split_type}')
        output.append(digit)

    if signal:
        output.append(signal)

    # The output is already inverted. If we want it to _not_ be inverted, then we invert it.
    if not invert_number:
        output = output[::-1]

    return ' '.join(output)


class T5Finetuner(pl.LightningModule):

    def __init__(self, hparams, train_dataloader, val_dataloader, test_dataloader, orthography):
        super(T5Finetuner, self).__init__()

        self.hparams = hparams

        self.tokenizer = AutoTokenizer.from_pretrained(self.hparams.model_name_or_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.hparams.model_name_or_path)

        if orthography.endswith('_fixed'):
            self.tokenizer.add_special_tokens({'additional_special_tokens': ['0']})

        self._train_dataloader = train_dataloader
        self._val_dataloader = val_dataloader
        self._test_dataloader = test_dataloader

    def prepare_batch(self, questions: List[str], answers: List[str]) -> List[str]:

        input_dict = self.tokenizer.batch_encode_plus(
            list(questions), padding=True, truncation=False, return_tensors='pt')

        labels = self.tokenizer.batch_encode_plus(
            list(answers), padding=True, truncation=False, return_tensors='pt')['input_ids']

        assert input_dict['input_ids'].shape[1] < self.hparams.max_seq_length
        assert labels.shape[1] < self.hparams.max_seq_length

        input_ids = input_dict['input_ids'].to(self.model.device)
        attention_mask = input_dict['attention_mask'].to(self.model.device)
        labels = labels.to(self.model.device)

        return input_ids, attention_mask, labels

    def forward(self, **kwargs):
        return self.model(**kwargs)

    def training_step(self, batch, batch_nb):
        questions, correct_answers = batch

        # Log every power of two.
        if batch_nb & (batch_nb - 1) == 0:
            print(questions[0])
            print(correct_answers[0])

        input_ids, attention_mask, labels = self.prepare_batch(
            questions=questions, answers=correct_answers)

        loss = self.model(input_ids=input_ids,
                          attention_mask=attention_mask,
                          labels=labels)[0]

        tensorboard_logs = {'train_loss': loss}
        return {'loss': loss, 'log': tensorboard_logs}

    def inference_step(self, batch, batch_nb: int):
        questions, correct_answers = batch

        input_ids, attention_mask, _ = self.prepare_batch(
            questions=questions, answers=correct_answers)

        batch_outputs = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            do_sample=False,
            max_length=self.hparams.max_seq_length)

        predicted_answers = [
            self.tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
            for output in batch_outputs]

        exact_matches = [
            compute_exact_match(predicted_answer=predicted_answer, correct_answer=correct_answer)
            for predicted_answer, correct_answer in zip(predicted_answers, correct_answers)]

        # Log every power of two.
        if batch_nb & (batch_nb - 1) == 0:
            print('\nQuestion:', questions[0])
            print('Correct:  ', correct_answers[0])
            print('Predicted:', predicted_answers[0].encode('utf-8'))
            print('Exact?', exact_matches[0])

        metrics = {'exact_matches': exact_matches}
        return metrics

    def validation_step(self, batch, batch_nb):
        return self.inference_step(batch, batch_nb)

    def test_step(self, batch, batch_nb):
        return self.inference_step(batch, batch_nb)

    def validation_epoch_end(self, outputs):
        exact_matches = []
        for x in outputs:
            exact_matches.extend(x['exact_matches'])
        exact_match = sum(exact_matches) / len(exact_matches)

        metrics = {'val_exact_match': exact_match}

        output = metrics.copy()
        output['progress_bar'] = metrics

        return output

    def test_epoch_end(self, outputs):
        exact_matches = []
        for x in outputs:
            exact_matches.extend(x['exact_matches'])
        exact_match = sum(exact_matches) / len(exact_matches)

        metrics = {'test_exact_match': exact_match}

        output = metrics.copy()
        output['progress_bar'] = metrics

        return output

    def train_dataloader(self):
        return self._train_dataloader

    def val_dataloader(self):
        return self._val_dataloader

    def test_dataloader(self):
        return self._test_dataloader

    def get_optimizer(self):
        optimizer_name = self.hparams.optimizer
        scheduler_name = self.hparams.scheduler
        lr = self.hparams.lr
        weight_decay = self.hparams.weight_decay

        optimizer = getattr(torch.optim, optimizer_name)

        # Prepare optimizer and schedule (linear warmup and decay)
        no_decay = ["bias", "LayerNorm.weight"]
        optimizer_grouped_parameters = [
            {
                "params": [p for n, p in self.model.named_parameters() if not any(nd in n for nd in no_decay)],
                "weight_decay": weight_decay,
            },
            {
                "params": [p for n, p in self.model.named_parameters() if any(nd in n for nd in no_decay)],
                "weight_decay": 0.0
            },
        ]
        optimizer = optimizer(optimizer_grouped_parameters, lr=lr, weight_decay=weight_decay)

        print(f'=> Using {optimizer_name} optimizer')

        if scheduler_name == 'StepLR':
            scheduler = torch.optim.lr_scheduler.StepLR(
                optimizer, step_size=self.hparams.step_size, gamma=self.hparams.gamma)
            print(f'=> Using StepLR (step_size = {self.hparams.step_size}, gamma = {self.hparams.gamma})')
        else:
            raise Exception(f'Scheduler not implemented: {scheduler_name}')

        return [optimizer], [scheduler]

    def configure_optimizers(self):
        optimizer = self.get_optimizer()
        return optimizer


class FinetuneDataset(Dataset):

    def __init__(self, examples: int):
        self.examples = examples
    
    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        numbers = self.examples[idx]['input']
        numbers_string = ', '.join(str(x) for x in numbers)
        sorted_numbers = sorted(numbers)
        sorted_numbers_string = ', '.join(str(x) for x in sorted_numbers)
        return f'The sorted ascending order of {numbers_string} is', sorted_numbers_string


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train and evalute T5 on arithmetic problems.')
    parser.add_argument('--output_dir', type=str, required=True, help='Path to save checkpoint and results.')
    parser.add_argument('--model_name_or_path', type=str, required=True)
    parser.add_argument('--operation', type=str, required=True, help='Either "addition" or "subtraction".')
    parser.add_argument(
        '--orthography', type=str, required=True,
        help='One of the following: "decimal, "character", "character_fixed", "underscore", "underscore_fixed", '
             '"words", "10based", or "10ebased"')
    parser.add_argument(
        '--invert_question', action='store_true',
        help="If passed, numbers in the question will be in the inverted order.")
    parser.add_argument(
        '--invert_answer', action='store_true',
        help="If passed, numbers in the answer will be in the inverted order.")
    parser.add_argument(
        '--balance_train', action='store_true',
        help='If passed, numbers the training set will be sampled using the "balanced" method described in the paper.'
             'Otherwise, the "random" method will be used.')
    parser.add_argument(
        '--balance_val', action='store_true',
        help='If passed, numbers the validation set will be sampled using the "balanced" method described in the paper.'
             'Otherwise, the "random" method will be used.')
    parser.add_argument(
        '--balance_test', action='store_true',
        help='If passed, numbers the test set will be sampled using the "balanced" method described in the paper.'
             'Otherwise, the "random" method will be used.')
    parser.add_argument(
        '--min_digits_train', type=int, default=2,
        help='Minimum number of digits sampled for training and validation examples.')
    parser.add_argument(
        '--min_digits_test', type=int, default=2,
        help='Minimum number of digits sampled for test examples.')
    parser.add_argument(
        '--max_digits_train', type=int, required=True,
        help='Maximum number of digits sampled for training and validation examples.')
    parser.add_argument(
        '--max_digits_test', type=int, required=True,
        help='Maximum number of digits sampled for test examples.')
    parser.add_argument(
        '--base_number', type=int, default=10,
        help="Base of the number (e.g.; 2 -> binary, 10 -> decimal).")
    parser.add_argument("--seed", default=123, type=int, help="Seed.")
    parser.add_argument("--train_size", default=1000, type=int, help="Number of examples for training.")
    parser.add_argument("--val_size", default=1000, type=int, help="Number of examples for training.")
    parser.add_argument("--test_size", default=2000, type=int, help="Number of examples for testing.")
    parser.add_argument('--max_seq_length', type=int, default=512, help='Maximum sequence length (in tokens).')
    parser.add_argument("--train_batch_size", default=8, type=int, help="Batch size per GPU/CPU for training.")
    parser.add_argument("--val_batch_size", default=8, type=int, help="Batch size per GPU/CPU for evaluation.")
    parser.add_argument('--optimizer', type=str, default='AdamW')
    parser.add_argument("--lr", default=5e-5, type=float, help="The initial learning rate for Adam.")
    parser.add_argument("--weight_decay", default=0.0, type=float, help="Weight decay if we apply some.")
    parser.add_argument('--scheduler', type=str, default='StepLR',
                        help='learning rate scheduler. Currently, only StepLR is supported.)')
    parser.add_argument('--gamma', type=float, default=0.1, help='gamma factor for ExponentialLR or StepLR')
    parser.add_argument('--step_size', type=int, default=2, help='period of learning rate decay (StepLR)')
    parser.add_argument('--t_0', type=int, default=2,
                        help='number of iterations for the first restart (CosineAnnealingWarmRestarts)')
    parser.add_argument('--t_mult', type=int, default=2,
                        help='a factor increases t_i after a restart (CosineAnnealingWarmRestarts)')
    parser.add_argument("--num_workers", default=4, type=int, help="Number of CPU workers for loading data.")

    parser = pl.Trainer.add_argparse_args(parser)

    args = parser.parse_args()

    print('args', args)

    os.makedirs(args.output_dir, exist_ok=True)

    random.seed(args.seed)
    pl.seed_everything(args.seed)

    with open('dataset_OOD.json', 'r') as f:
        data = json.load(f)
    
    dataset_len = args.train_size + args.val_size + args.test_size
    data_asc = random.sample(list(filter(lambda x: x['asc'] == True, data)), dataset_len//2)
    data_desc = random.sample(list(filter(lambda x: x['asc'] == False, data)), dataset_len//2)

    data_train_asc, data_test_asc = random_split(data_asc, [(args.train_size + args.val_size)//2, args.test_size//2])
    data_train_asc, data_val_asc = random_split(data_train_asc, [args.train_size//2, args.val_size//2])

    data_train_desc, data_test_desc = random_split(data_desc, [(args.train_size + args.val_size)//2, args.test_size//2])
    data_train_desc, data_val_desc = random_split(data_train_desc, [args.train_size//2, args.val_size//2])

    dataset_train = FinetuneDataset(data_train_asc + data_train_desc)
    dataset_val = FinetuneDataset(data_val_asc + data_val_desc)
    dataset_test = FinetuneDataset(data_test_asc + data_test_desc)

    train_dataloader = DataLoader(dataset_train, batch_size=args.train_batch_size, shuffle=True, num_workers=args.num_workers)

    val_dataloader = DataLoader(dataset_val, batch_size=args.val_batch_size, shuffle=False, num_workers=args.num_workers)

    test_dataloader = DataLoader(dataset_test, batch_size=args.val_batch_size, shuffle=False, num_workers=args.num_workers)

    checkpoint_callback = ModelCheckpoint(
        filepath=os.path.join(args.output_dir, 'main-{epoch}-{val_exact_match:.4f}'),
        verbose=False, save_last=False, save_top_k=1, mode='max', monitor='val_exact_match',
        save_weights_only=False, period=args.check_val_every_n_epoch)

    trainer = pl.Trainer.from_argparse_args(args, checkpoint_callback=checkpoint_callback)

    # model = T5Finetuner(hparams=args,
    #                     train_dataloader=train_dataloader,
    #                     val_dataloader=val_dataloader,
    #                     test_dataloader=test_dataloader,
    #                     orthography=args.orthography)

    # trainer.fit(model)

    checkpoint_path = glob.glob(os.path.join(args.output_dir, 'finetune-*.ckpt'))[0]
    model = T5Finetuner.load_from_checkpoint(checkpoint_path,
                                             train_dataloader=train_dataloader,
                                             val_dataloader=val_dataloader,
                                             test_dataloader=test_dataloader,
                                             orthography=args.orthography)

    results = trainer.test(model)

    output = {'seed': args.seed,
              'max_digits_train': args.max_digits_train,
              'max_digits_test': args.max_digits_test,
              'test_exact_match': results[0]['test_exact_match']}

    with open(os.path.join(args.output_dir, 'ood_results.json'), 'w') as fout:
        json.dump(output, fout)

    print('OOD Testing Done!')
