[切换到中文版本](README_zh.md) 

[Switch to English Version](README.md)
# 无名杀AI

无名杀ai/无名杀AI相关项目，该项目涉及AI程序，旨在通过输入技能效果，生成无名杀技能代码。  
[modelscope（魔搭社区）在线体验](https://www.modelscope.cn/studios/huskyhong/nonameai)  
因为算力有限，在线体验版本仅为轻量cpu版，精度有限，如有需求请选择gpu版、完整版进行推理
finetuned from QWen
## 配置要求

为了更好地满足使用需求，请尽可能满足以下要求:

- 电脑（必须）
- 硬盘存储空间20G以上（必须）
- 若使用完整非量化版本/gpu版懒人一键包，对于具有 NVIDIA 显卡的电脑，采用gpu推理，要求显存 + 电脑物理内存（物理内存不包含虚拟内存）的一半 >= 16G
- 若使用完整非量化版本/cpu版懒人一键包，采用cpu方式推理，对于无显卡的电脑，要求内存（可包含虚拟内存）尽可能满足 >= 32G
- 若使用轻量版/gpu版轻量版懒人一键包，对于具有 NVIDIA 显卡的电脑，采用gpu推理，要求显存 + 电脑物理内存（物理内存不包含虚拟内存）的一半 >= 4G
- 若使用轻量版/cpu版轻量版懒人一键包，采用cpu方式推理，对于无显卡的电脑，要求内存（可包含虚拟内存）尽可能满足 >= 12G

## 使用方法
### 完整模型法
1. 安装 Python 以及相应的 Python 编译器
  - 注意：python适配版本为3.8,3.9,3.10,3.11，请勿安装过高或过低版本
2. 在终端（命令行）中输入以下命令安装依赖环境:

   ```bash
   pip install -r requirements.txt
   ```
3. 采用以下python代码运行程序，模型将会自动下载，v3.x模型代码运行方式如下：
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "huskyhong/noname-ai-v3.0"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "请帮我用JavaScript编写一个无名杀游戏的技能，技能效果如下：你使用杀造成的伤害+1"
# prompt = "请帮我用JavaScript编写一张无名杀游戏的卡牌，卡牌效果如下：xxx"
messages = [
    {"role": "system", "content": "你是由B站up主AKA臭脸臭羊驼训练得到的无名杀AI，旨在帮助用户编写无名杀技能或卡牌代码."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

v2.x,v1.x代码运行方式如下  

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
tokenizer = AutoTokenizer.from_pretrained("huskyhong/noname-ai-v2_5", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("huskyhong/noname-ai-v2_5", device_map="auto", trust_remote_code=True).eval() # 采用gpu加载模型
# model = AutoModelForCausalLM.from_pretrained("huskyhong/noname-ai-v2_5", device_map="cpu", trust_remote_code=True).eval() # 采用cpu加载模型
model.generation_config = GenerationConfig.from_pretrained("huskyhong/noname-ai-v2_5", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参
# 第一代模型请将huskyhong/noname-ai-v2_5改为huskyhong/noname-ai-v1，轻量版v2.5模型请将huskyhong/noname-ai-v2_5改为huskyhong/noname-ai-v2_5-light

prompt = "请帮我编写一个技能，技能效果如下：" + input("请输入技能效果：")
response, history = model.chat(tokenizer, prompt, history = [])
print(response)

prompt = "请帮我编写一张卡牌，卡牌效果如下：：" + input("请输入卡牌效果：")
response, history = model.chat(tokenizer, prompt, history = [])
print(response)
```
也可以采用huggingface的pipeline进行推理
```python
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, GenerationConfig
generator = pipeline(
    "text-generation",
    model="huskyhong/noname-ai-v2_5",
    tokenizer="huskyhong/noname-ai-v2_5",
    device=0,  # 选择GPU设备，如果要使用CPU，可以设置device=-1
    trust_remote_code=True
)

prompt = "请帮我编写一个技能，技能效果如下：" + input("请输入技能效果：")
response = generator(prompt, max_length=50, top_p=0.95)  # 可根据需要调整生成长度、top_p等超参数)
print(response[0]['generated_text'])

prompt = "请帮我编写一张卡牌，卡牌效果如下：" + input("请输入卡牌效果：")
response = generator(prompt, max_length=50, top_p=0.95)  # 可根据需要调整生成长度、top_p等超参数
print(response[0]['generated_text'])
```

4. 如果自动下载出错，可以手动下载模型文件，同时修改代码中的"huskyhong/noname-ai-v2"为相应位置
   第三代模型下载地址:
   - [v3.0版本huggingface地址（完整版）](https://huggingface.co/huskyhong/noname-ai-v2_5)
   - [v3.0版本huggingface地址（普通版）](https://huggingface.co/huskyhong/noname-ai-v2_5-medium)
   - [v3.0版本huggingface地址（轻量版）](https://huggingface.co/huskyhong/noname-ai-v2_5-light)
   - [v3.0版本huggingface地址（迷你版）](https://huggingface.co/huskyhong/noname-ai-v2_5-mini)
   - [百度网盘地址](https://pan.baidu.com/s/1zIcRZtQv5oIdu7_abie9Vw?pwd=6666) 百度网盘提取码：6666
      第二代模型下载地址:
   - [v2.5版本huggingface地址（完整版）](https://huggingface.co/huskyhong/noname-ai-v2_5)
   - [v2.5版本huggingface地址（轻量版）](https://huggingface.co/huskyhong/noname-ai-v2_5-light)
   - [百度网盘地址](https://pan.baidu.com/s/1m9RfGqnuQbRYROE_UzuG-Q?pwd=6666) 百度网盘提取码：6666   
     第一代模型下载地址:
   - [huggingface地址](https://huggingface.co/huskyhong/noname-ai-v1)
   - [百度网盘地址](https://pan.baidu.com/s/1Ox471XuHF_gJbcPPnSZe7g?pwd=6666) 百度网盘提取码：6666 
记得选择采用gpu加载模型还是cpu加载模型，然后把 `your_model_name` 替换为你实际的模型路径。

## 懒人一键包
- 一键安装，无需烦恼
- 请根据自身配置选择合适的懒人一键包
- [懒人一键包百度网盘下载地址（已更新v3.0）](https://pan.baidu.com/s/1zIcRZtQv5oIdu7_abie9Vw?pwd=6666) 百度网盘提取码：6666
- [懒人一键包123网盘下载地址（已更新v2.5）](https://www.123pan.com/s/lOcnjv-pnOG3.html) 123网盘提取码:6666
- 请注意懒人一键包版本时间，确保版本为最新版！
- 懒人包相关视频
- [懒人包v2.5版效果对比]([https://www.bilibili.com/video/BV1KKY4e8EaC]
## 网页版/服务器部署
   - 安装 Python 
   - 安装依赖环境
   ```bash
   pip install -r requirements.txt
   ```
  - 安装streamlit
   ```bash
   pip install streamlit
   ```
   - 服务器放行8501端口（也可自行改成其他，需要和webdemo.py文件中对应）
   - 运行webdemo
   ```bash
   streamlit run webdemo.py
   ```

## 训练/微调  
训练/微调需要安装新的依赖项
```python
pip install peft deepspeed
```
克隆该项目，并下载v2.3版本的模型文件，以轻量版为例：
```bash
git lfs install
git clone https://github.com/204313508/noname_llm.git
git clone https://huggingface.co/huskyhong/noname-ai-v2_3-light
cd noname_llm/finetune
```  
修改finetune.sh中训练所需参数，模型、数据集位置等信息，之后输入以下命令开始训练  
```bash
bash finetune.sh
```
详细步骤请参考[微调说明](./finetune/README.md)

## 网页版/服务器示例
![webdemo1](./webdemo1.png)
![webdemo2](./webdemo2.png)
## 注意事项

- AI生成受不可控因素影响，生成的代码不保证100%有效，仍可能出现bug、冗余代码或额外特殊符号等，需要人工修改。
- （重要）遵循AI规范，本AI模型仅用于学习交流使用，请勿用于不法用途以及商业用途。本人发布该模型初衷是希望大家更好地学习和交流，模型涉及的所有相关信息都是公开的。对于恶意使用本AI模型的，本人概不负责。

## 其他内容

如果有相关问题，请在GitHub官方的issue中提出。

## 演示图片
该演示图片基于v3.x启动器发布  
![demo1](./demo.png)

## 赞助
- 厚颜无耻的求一个赞助
![sponsor](./sponsor.jpg)
