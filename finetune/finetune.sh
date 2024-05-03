#!/bin/bash
export CUDA_DEVICE_MAX_CONNECTIONS=1
DIR=`pwd`


MODEL="/tmp/pretrainmodel/nonameai"
DATA="/tmp/code/data.json"

export CUDA_VISIBLE_DEVICES=0

python finetune.py \
  --model_name_or_path $MODEL \
  --data_path $DATA \
  --bf16 True \
  --output_dir /tmp/pretrainmodel/nonameai \
  --num_train_epochs 5 \
  --per_device_train_batch_size 2 \
  --per_device_eval_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --evaluation_strategy "no" \
  --save_strategy "steps" \
  --max_steps 2000 \
  --save_steps 500 \
  --save_total_limit 10 \
  --learning_rate 3e-4 \
  --weight_decay 0.1 \
  --adam_beta2 0.95 \
  --warmup_ratio 0.01 \
  --lr_scheduler_type "cosine" \
  --logging_steps 10 \
  --report_to "none" \
  --model_max_length 2048 \
  --lazy_preprocess True \
  --gradient_checkpointing \
  --use_lora

