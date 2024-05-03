[切换到中文版本](README_zh.md) 

[Switch to English Version](README.md)
# Noname AI 模型微调

## 简介

本仓库包含了在自定义数据集上对 Noname AI 模型进行微调的脚本。在开始微调过程之前，请确保已安装所需的依赖项并获取了必要的模型和数据集文件。

## 依赖项

运行以下命令安装所需的依赖项：

```bash
pip install peft deepspeed
```

## 设置

1. 克隆此仓库：

```bash
git clone https://github.com/204313508/noname_llm.git
cd noname_llm/finetune
```

2. 从 Hugging Face 克隆 v2.3 版本的模型文件：

```bash
git lfs install
git clone https://huggingface.co/huskyhong/noname-ai-v2_3-light
```

3. 设置环境变量并根据您的需求调整训练脚本 (`finetune.py`) 中的参数：

```bash
export CUDA_DEVICE_MAX_CONNECTIONS=1
export CUDA_VISIBLE_DEVICES=0

MODEL="/tmp/pretrainmodel/nonameai"
DATA="/tmp/code/data.json"
```

## 数据集格式

数据集以 JSON 格式存储，示例如下：

```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "请帮我编写一个技能，技能效果如下：你的技能效果描述"
      },
      {
        "from": "assistant",
        "value": "你的技能代码"
      }
    ]
  },
  {
    "id": "identity_1",
    "conversations": [
      {
        "from": "user",
        "value": "请帮我编写一个技能，技能效果如下：你的技能效果描述"
      },
      {
        "from": "assistant",
        "value": "你的技能代码"
      }
    ]
  },
  ...
]
```



## 参数修改说明

在 `finetune.py` 脚本中，您可以根据您的任务需求调整以下参数：

- `--model_name_or_path`：指定模型的路径或名称。
- `--data_path`：指定数据集的路径。
- `--num_train_epochs`：指定训练的轮数。
- `--per_device_train_batch_size`：指定每个设备的训练批次大小。
- `--per_device_eval_batch_size`：指定每个设备的评估批次大小。
- `--max_steps`：指定训练的最大步数。
- `--learning_rate`：指定学习率。
- `--weight_decay`：指定权重衰减。


## 训练

运行以下命令开始微调过程：

```bash
bash finetune.sh
```
