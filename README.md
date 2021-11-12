# cse576-nlp-project7-team3


## TASK : SORTING - ASCENDING AND DESCENDING


First, install the required packages:
```
pip install -r requirements.txt
```

The command below trains and evaluates the Finetuner model:

```
python "finetuner.py" \
    --data_dir='datatset_finetune/sort_99' \
    --output_dir='./models/finetune' \
    --model_name_or_path=t5-base \
    --ckpt_path='{path-to-checkpoint}' \
    --model_prefix=finetune \
    --sort_type=asc \
    --seed=1 \
    --train_size=1000 \
    --val_size=1000 \
    --test_size=1000 \
    --train_batch_size=4 \
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
    --max_epochs=20

```

Pass the ckpt_path argument only if you want to load a pretrained model.
