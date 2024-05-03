[Switch to Chinese Version](README_zh.md)

# Noname AI Model Fine-tuning

## Introduction

This repository contains scripts for fine-tuning the Noname AI model on custom datasets. Before starting the fine-tuning process, make sure you have installed the necessary dependencies and obtained the required model and dataset files.

## Dependencies

Run the following command to install the required dependencies:

```bash
pip install peft deepspeed
```

## Setup

1. Clone this repository:

```bash
git clone https://github.com/204313508/noname_llm.git
cd noname_llm/finetune
```

2. Clone the model files of version v2.3 from Hugging Face:

```bash
git lfs install
git clone https://huggingface.co/huskyhong/noname-ai-v2_3-light
```

3. Set environment variables and adjust the parameters in the training script (`finetune.sh`) according to your requirements:

```bash
export CUDA_DEVICE_MAX_CONNECTIONS=1
export CUDA_VISIBLE_DEVICES=0

MODEL="/tmp/pretrainmodel/nonameai"
DATA="/tmp/code/data.json"
```

## Dataset Format

The dataset is stored in JSON format, as shown below:

```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "Please help me write a skill, the skill effect is as follows: your skill effect description"
      },
      {
        "from": "assistant",
        "value": "Your skill code"
      }
    ]
  },
  {
    "id": "identity_1",
    "conversations": [
      {
        "from": "user",
        "value": "Please help me write a skill, the skill effect is as follows: your skill effect description"
      },
      {
        "from": "assistant",
        "value": "Your skill code"
      }
    ]
  },
  ...
]
```

## Parameter Modification Instructions

In the `finetune.py` script, you can adjust the following parameters according to your task requirements:

- `--model_name_or_path`: Specify the path or name of the model.
- `--data_path`: Specify the path of the dataset.
- `--num_train_epochs`: Specify the number of training epochs.
- `--per_device_train_batch_size`: Specify the training batch size per device.
- `--per_device_eval_batch_size`: Specify the evaluation batch size per device.
- `--max_steps`: Specify the maximum number of training steps.
- `--learning_rate`: Specify the learning rate.
- `--weight_decay`: Specify the weight decay.

## Fine-tuning

Run the following command to start the fine-tuning process:

```bash
bash finetune.sh
```
