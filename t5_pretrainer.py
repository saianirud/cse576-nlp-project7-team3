import argparse
import glob
import json
import pytorch_lightning as pl
import random
import os
from pytorch_lightning.callbacks import ModelCheckpoint
from torch.utils.data import Dataset, DataLoader
import jsonlines

from utils import T5 as T5Pretrainer, convert_to_ebased, convert_to_10based, convert_to_10ebased


class PretrainDataset(Dataset):

    def __init__(self, data_dir, type_path, sort_type, data_size, representation=None,  separator=None, span_length=None):

        self.data = []
        self.examples = []

        self.representation = representation
        self.span_length = span_length
        self.separator = separator if separator else ' '

        if sort_type == 'asc':
            self.sort_type = 'asc'
        else:
            self.sort_type = 'desc'

        for root, dirs, files in os.walk(data_dir):
            for file in files:
                if file == type_path+'.jsonl':
                    self.path = os.path.join(root, file)
                    with jsonlines.open(self.path) as f:
                        for each in f:
                            self.data.append(each)
        
        random.shuffle(self.data)

        if self.span_length:
            self.data = list(filter(lambda x: len(x['numbers']) > self.span_length+1, self.data))
        
        self.examples = self.data
        if data_size != 0:
            indexes = random.sample(range(0, len(self.data)), data_size)
            self.examples = [self.data[i] for i in indexes]
        
        random.shuffle(self.examples)
    
    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        '''
            Take a span of numbers and rearrange them in sorted order keeping the remaining numbers same. This helps the model to sort the numbers.

            Original: The sorted ascending order of 60 12 91 43 63 15 33 47 69 is 60 12 43 63 91 15 33 47 69
            Input: The sorted ascending order of 60 12 91 43 63 15 33 47 69 is 60 12 <extra_id_0> <extra_id_1> <extra_id_2> 15 33 47 69
            label: 43 63 91
        '''
        
        numbers = self.examples[idx]['numbers']

        span_length = self.span_length if self.span_length else random.choice(range(3, len(numbers)-1)) if len(numbers) > 4 else 2
        span_start = random.choice(range(len(numbers) - span_length + 1))
        span_end = span_start + span_length
        span_numbers = numbers[span_start:span_end]

        if self.sort_type == 'asc':
            span_numbers = sorted(span_numbers)
            sort_type = 'ascending'
        else:
            span_numbers = sorted(span_numbers, reverse=True)
            sort_type = 'descending'
        
        numbers = self.convert_numbers(numbers)
        span_numbers = self.convert_numbers(span_numbers)

        label = ''
        i = 0
        for i in range(len(span_numbers)):
            label += '<extra_id_{0}>{1}'.format(i, span_numbers[i])
            span_numbers[i] = '<extra_id_{0}>'.format(i)
        label += '<extra_id_{0}>'.format(i+1)
        result_numbers = numbers[:span_start] + span_numbers + numbers[span_end:]
        
        numbers_string = self.separator.join(str(x) for x in numbers)
        result_string = self.separator.join(str(x) for x in result_numbers)
        
        input = 'The sorted '+ sort_type +' order of ' + numbers_string + ' is ' + result_string
        
        return input, label

    def convert_numbers(self, numbers: list) -> list:

        if self.representation == 'ebased':
            return [convert_to_ebased(str(number)) for number in numbers]
        elif self.representation == '10ebased':
            return [convert_to_10ebased(str(number)) for number in numbers]
        elif self.representation == '10based':
            return [convert_to_10based(str(number)) for number in numbers]
        else:
            return [str(number) for number in numbers]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Train and evalute T5 on arithmetic problems.')
    parser.add_argument('--data_dir', type=str, required=True, help='Path to take data from.')
    parser.add_argument('--output_dir', type=str, default='./models/pretrain', required=False, help='Path to save checkpoint and results.')
    parser.add_argument('--model_name_or_path', type=str, required=True)
    parser.add_argument('--model_prefix', type=str, default='pretrain', help='Prefix of Output Model')
    parser.add_argument('--sort_type', type=str, default='asc', help='asc for Ascending and desc for descending')
    parser.add_argument("--seed", default=123, type=int, help="Seed.")
    parser.add_argument("--train_size", default=0, type=int, help="Number of examples for training.")
    parser.add_argument("--val_size", default=0, type=int, help="Number of examples for training.")
    parser.add_argument("--test_size", default=0, type=int, help="Number of examples for testing.")
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
    parser.add_argument("--representation", default=None, type=str, help="Number representation")
    parser.add_argument("--span_length", default=None, type=int, help="Length of span to mask")
    parser.add_argument("--separator", default=None, type=str, help="Separator")

    parser = pl.Trainer.add_argparse_args(parser)

    args = parser.parse_args()

    print('args', args)

    os.makedirs(args.output_dir, exist_ok=True)

    random.seed(args.seed)
    pl.seed_everything(args.seed)


    '''
        Pretraining the model
    '''

    dataset_train = PretrainDataset(args.data_dir, 'train', args.sort_type, args.train_size, args.representation, args.separator, args.span_length)
    dataset_val = PretrainDataset(args.data_dir, 'val', args.sort_type, args.val_size, args.representation, args.separator, args.span_length)
    dataset_test = PretrainDataset(args.data_dir, 'test', args.sort_type, args.test_size, args.representation, args.separator, args.span_length)

    train_dataloader = DataLoader(dataset_train, batch_size=args.train_batch_size, shuffle=True, num_workers=args.num_workers)
    val_dataloader = DataLoader(dataset_val, batch_size=args.val_batch_size, shuffle=False, num_workers=args.num_workers)
    test_dataloader = DataLoader(dataset_test, batch_size=args.val_batch_size, shuffle=False, num_workers=args.num_workers)

    checkpoint_callback = ModelCheckpoint(
        filepath=os.path.join(args.output_dir, args.model_prefix + '-{epoch}-{val_exact_match:.4f}'),
        verbose=False, save_last=True, save_top_k=1, mode='max', monitor='val_exact_match',
        save_weights_only=False, period=args.check_val_every_n_epoch)

    trainer = pl.Trainer.from_argparse_args(args, checkpoint_callback=checkpoint_callback)
    model = T5Pretrainer(hparams=args, train_dataloader=train_dataloader, val_dataloader=val_dataloader, test_dataloader=test_dataloader)

    trainer.fit(model)


    '''
        Testing the model
    '''

    checkpoint_path = glob.glob(os.path.join(args.output_dir, args.model_prefix + '-*.ckpt'))[0]
    model = T5Pretrainer.load_from_checkpoint(checkpoint_path, train_dataloader=train_dataloader, val_dataloader=val_dataloader, test_dataloader=test_dataloader)

    results = trainer.test(model)

    output = {
        'seed': args.seed,
        'model': args.model_name_or_path,
        'sort_type': args.sort_type,
        'train_size': args.train_size,
        'val_size': args.val_size,
        'test_size': args.test_size,
        'test_exact_match': results[0]['test_exact_match'],
        'test_loss': results[0]['test_loss'],
        'batch_size': args.train_batch_size
    }

    with open(os.path.join(args.output_dir, 'pretrain_results.json'), 'w') as fout:
        json.dump(output, fout)

    print('Pretraining Done!')