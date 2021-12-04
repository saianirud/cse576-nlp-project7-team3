# cse576-nlp-project7-team3


## TASK : SORTING - ASCENDING AND DESCENDING

## Different Strategies

### Span Masking

Take a continuous span of numbers and rearrange them in sorted order keeping the remaining numbers same. This helps the model to sort the numbers.</br>
`Original: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|43|63|91|15|33|47|69`</br>
`Input: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|<extra_id_0>|<extra_id_1>|<extra_id_2>|15|33|47|69`</br>
`label: 43|63|91`</br>
The length of span is mentioned in the comments column. It is 3 for above example.
​

### Yes/No Classification

Classify whether the given list of numbers in the input sentence are correctly sorted into mentioned order.</br>
`Input: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 12|15|33|43|47|60|63|69|91`</br>
`label: Yes`</br>
`Input: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|43|63|91|15|33|47|69`</br>
`label: No`</br>

### E-based Representation

`Numbers: 60|12|91`</br>
`Input: Sort in ascending order: 6 e 1 0 e 0|1 e 1 2 e 0|9 e 1 1 e 0`</br>
`label: 1 e 1 2 e 0|4 e 1 3 e 0|9 e 1 1 e 0`
​
### 10e-based Representation

`Numbers: 60|12|91`</br>
`Input: Sort in ascending order: 6 10e1 0 10e0|1 10e1 2 10e0|9 10e1 1 10e0`</br>
`label: 1 10e1 2 10e0|4 10e1 3 10e0|9 10e1 1 10e0`

### 10-based Representation

`Numbers: 60|12|91`</br>
`Input: Sort in ascending order: 6 10 0 1|1 10 2 1|9 10 1 1`</br>
`label: 1 10 2 1|4 10 3 1|9 10 1 1`
​
### Number Masking

`Numbers: 60|12|91`</br>
`Input: The sorted ascending order of 6555|6173|423|108 is 108|<extra_id_0>|<extra_id_1>|<extra_id_2>`</br>
`label: 423|6173|6555`
​
### Digit Masking

`Numbers: 12 7 33`</br>
`Input: The sorted ascending order of 12 7 33 is 7 <mask_1>2 <mask_2>3`</br>
`label: 1 3`

### Native Language Modelling

`Numbers: ४५ ३ ७९` </br>
`Input: Sort in ascending order: ४५ ३ ७९`</br>
`label: ३ ४५ ७९`

## Best performing models



## How to run the code

### Go to the project directory:
```
cd /content/drive/MyDrive/Colab Notebooks/cse576-nlp-project7-team3
```

### Install the required packages:
```
pip install -r requirements.txt
```

### The command below tests and evaluates the Finetuned model:

```

!python "test.py" \
    --data_dir='dataset_finetune/sort_9999/5' \
    --output_dir='models/finetune' \
    --model_name_or_path=t5-base \
    --ckpt_path='/content/drive/MyDrive/Colab Notebooks/cse576-nlp-project7-team3/models/finetune/model.ckpt' \
    --model_prefix=finetune \
    --sort_type=asc \
    --seed=1 \
    --train_size=10000 \
    --val_size=1000 \
    --test_size=1000 \
    --train_batch_size=16 \
    --val_batch_size=32 \
    --max_seq_length=512 \
    --optimizer=AdamW \
    --lr=3e-4 \
    --weight_decay=5e-5 \
    --scheduler=StepLR \
    --gamma=1.0 \
    --step_size=1000 \
    --t_0=2 \
    --t_mult=2 \
    --num_workers=4 \
    --accumulate_grad_batches=32 \
    --gpus=1 \
    --check_val_every_n_epoch=2 \
    --amp_level=O0 \
    --precision=32 \
    --gradient_clip_val=1.0 \
    --max_epochs=20 \
    --representation=10based \
    --separator='|'

```
#### Params
`data_dir`: Path to the dataset. The directory should contains 4 files with the following names i.e. `train.jsonl`, `val.jsonl`, `test.jsonl`, `expol_test.jsonl`</br>
`output_dir`: Path where the model creates the checkpoint.</br>
`ckpt_path`: Path to checkpoint to load a finetuned model.</br>
`representation`: There are 3 types of representations i.e. `ebased`, `10ebased`, `10based`. If no representation is given, default will be `decimal`. Do not pass the `representation` arg if you want `decimal` representation.</br>
`separator`: Pass the separator you want to separate the numbers. If no separator is given, Default will be `' '`</br>
`sort_type`: There are 3 types of representations i.e. `asc`, `desc`.</br>
`model_prefix`: The model checkpoint name starts with this prefix.</br>


### The command below trains and evaluates the Pretrained model:

```

!python "t5_finetuner.py" \
    --data_dir='dataset_finetune/sort_9999/5' \
    --output_dir='models/finetune' \
    --model_name_or_path=t5-base \
    --ckpt_path='/content/drive/MyDrive/Colab Notebooks/cse576-nlp-project7-team3/models/finetune/model.ckpt' \
    --model_prefix=finetune \
    --sort_type=asc \
    --seed=1 \
    --train_size=10000 \
    --val_size=1000 \
    --test_size=1000 \
    --train_batch_size=16 \
    --val_batch_size=32 \
    --max_seq_length=512 \
    --optimizer=AdamW \
    --lr=3e-4 \
    --weight_decay=5e-5 \
    --scheduler=StepLR \
    --gamma=1.0 \
    --step_size=1000 \
    --t_0=2 \
    --t_mult=2 \
    --num_workers=4 \
    --accumulate_grad_batches=32 \
    --gpus=1 \
    --check_val_every_n_epoch=2 \
    --amp_level=O0 \
    --precision=32 \
    --gradient_clip_val=1.0 \
    --max_epochs=20 \
    --representation=10based \
    --separator='|'

```
#### Params
`data_dir`: Path to the dataset. The directory should contains 4 files with the following names i.e. `train.jsonl`, `val.jsonl`, `test.jsonl`, `expol_test.jsonl`</br>
`output_dir`: Path where the model creates the checkpoint.</br>
`ckpt_path`: Pass the `ckpt_path argument` only if you want to load a pretrained model.</br>
`representation`: There are 3 types of representations i.e. `ebased`, `10ebased`, `10based`. If no representation is given, default will be `decimal`. Do not pass the `representation` arg if you want `decimal` representation.</br>
`separator`: Pass the separator you want to separate the numbers. If no separator is given, Default will be `' '`</br>
`sort_type`: There are 3 types of representations i.e. `asc`, `desc`.</br>
`model_prefix`: The model checkpoint name starts with this prefix.</br>
