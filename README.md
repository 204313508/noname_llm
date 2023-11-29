# 无名杀AI

该项目旨在通过输入技能效果，生成无名杀技能代码的AI。

## 配置要求

为了更好地满足使用需求，请尽可能满足以下要求:

- 电脑（必须）
- 硬盘存储空间20G以上（必须）
- 对于具有 NVIDIA 显卡的电脑，要求显存 + 电脑内存的一半 >= 16G
- 对于无显卡的电脑，要求内存尽可能满足 >= 32G

## 使用方法

1. 安装 Python 以及相应的 Python 编译器
2. 在终端（命令行）中输入以下命令安装依赖环境:

   ```bash
   pip install -r requirements.txt
   ```

3. 下载模型文件并放入 `model` 文件夹中，最终目录应为 `xx/model/QWen-7B-Chat`

   模型下载地址:
   - [huggingface地址](https://huggingface.co/Qwen/Qwen-7B-Chat)
   - [百度网盘地址](https://pan.baidu.com/s/1OrB_dEACkyhp-iOkP2RkJg?pwd=6666) 百度网盘提取码：6666

4. 下载权重文件并放入 `checkpoint` 文件夹中，最终目录应为 `xx/model/版本`

   checkpoint 下载地址，请选择合适的版本进行下载:
   - [百度网盘地址](https://pan.baidu.com/s/1nugDoRroD2I0dX3fcP9umA?pwd=6666) 百度网盘提取码：6666

5. 运行 Python 脚本:

   ```bash
   python demo.py
   ```

## 注意事项

- 0.4k版本为测试版，训练数据极少，仅用于测试，仅支持生成单技能，暂不支持生成多个技能连携的代码。生成的代码效果无法保证，如有需求请期待后续正式版本以及定制版本。
- AI生成受不可控因素影响，生成的代码不保证100%有效，仍可能出现bug、冗余代码或额外的双引号等，需要人工修改。
- （重要）遵循AI规范，本AI模型仅用于学习交流使用，请勿用于不法用途以及商业用途。本人发布该模型初衷是希望大家更好地学习和交流，模型涉及的所有相关信息都是公开的。对于恶意使用本AI模型的，本人概不负责。

## 其他内容

如果有相关问题，请在GitHub官方的issue中提出。

## 演示图片

![demo1](./demo1.jpg)
![demo2](./demo2.jpg)
![demo3](./demo3.jpg)

## 赞助
- 厚颜无耻的求一个赞助
![sponsor](./sponsor.jpg)
