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
3. 采用以下python代码运行程序，模型将会自动下载，代码默认为v2.0完整版
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
tokenizer = AutoTokenizer.from_pretrained("huskyhong/noname-ai-v2", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("huskyhong/noname-ai-v2", device_map="auto", trust_remote_code=True).eval() # 采用gpu加载模型
# model = AutoModelForCausalLM.from_pretrained("huskyhong/noname-ai-v2", device_map="cpu", trust_remote_code=True).eval() # 采用cpu加载模型
model.generation_config = GenerationConfig.from_pretrained("huskyhong/noname-ai-v2", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参
# 第一代模型请将huskyhong/noname-ai-v2改为huskyhong/noname-ai-v1，轻量版v2.3模型请将huskyhong/noname-ai-v2改为huskyhong/noname-ai-v2_3-light

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
    model="huskyhong/noname-ai-v2",
    tokenizer="huskyhong/noname-ai-v2",
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
      第二代模型下载地址:
   - [v2.0版本huggingface地址（完整版）](https://huggingface.co/huskyhong/noname-ai-v2)
   - [v2.3版本huggingface地址（轻量版）](https://huggingface.co/huskyhong/noname-ai-v2_3-light)
   - [百度网盘地址](https://pan.baidu.com/s/1m9RfGqnuQbRYROE_UzuG-Q?pwd=6666) 百度网盘提取码：6666   
     第一代模型下载地址:
   - [huggingface地址](https://huggingface.co/huskyhong/noname-ai-v1)
   - [百度网盘地址](https://pan.baidu.com/s/1Ox471XuHF_gJbcPPnSZe7g?pwd=6666) 百度网盘提取码：6666 
记得选择采用gpu加载模型还是cpu加载模型，然后把 `your_model_name` 替换为你实际的模型路径。

## 懒人一键包
- 一键安装，无需烦恼
- 请根据自身配置选择合适的懒人一键包
- [懒人一键包百度网盘下载地址（已更新v2.3）](https://pan.baidu.com/s/1zIcRZtQv5oIdu7_abie9Vw?pwd=6666) 百度网盘提取码：6666
- [懒人一键包123网盘下载地址（已更新v2.3）](https://www.123pan.com/s/lOcnjv-pnOG3.html) 123网盘提取码:6666
- 请注意懒人一键包版本时间，确保版本为最新版！
- 懒人包相关视频
- [懒人包v2.3版效果对比](https://www.bilibili.com/video/BV1at421V7Qu)
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
   
## 网页版/服务器示例
![webdemo1](./webdemo1.png)
![webdemo2](./webdemo2.png)
## 注意事项

- AI生成受不可控因素影响，生成的代码不保证100%有效，仍可能出现bug、冗余代码或额外特殊符号等，需要人工修改。
- （重要）遵循AI规范，本AI模型仅用于学习交流使用，请勿用于不法用途以及商业用途。本人发布该模型初衷是希望大家更好地学习和交流，模型涉及的所有相关信息都是公开的。对于恶意使用本AI模型的，本人概不负责。

## 其他内容

如果有相关问题，请在GitHub官方的issue中提出。

## 演示图片
该演示图片基于v1.0发布
![demo1](./demo1.jpg)
![demo2](./demo2.jpg)
![demo3](./demo3.jpg)

## 赞助
- 厚颜无耻的求一个赞助
![sponsor](./sponsor.jpg)
