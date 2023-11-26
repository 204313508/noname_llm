#无名杀AI
AI生成无名杀技能代码。只要输入技能效果，AI生成技能代码
##配置要求
为了更好的满足使用需要，请您尽可能满足以下要求  
<li>电脑（必须）  
<li>硬盘存储空间20G以上（必须）
<li>对于具有nvidia显卡的电脑 要求显存+电脑内存的一半>=16G
<li>对于无显卡的电脑 要求内存尽可能满足>=32G
##使用方法
<li>安装python以及相应的python编译器
<li>安装依赖的环境，在终端（命令行）中输入  
``pip install -r requirements.txt``
<li>下载模型文件并放入model文件夹中，最终完成的目录应该是xx/model/QWen-7B-Chat  
模型下载地址  
[huggingface地址](https://huggingface.co/Qwen/Qwen-7B-Chat) [百度网盘地址](链接：https://pan.baidu.com/s/1OrB_dEACkyhp-iOkP2RkJg?pwd=6666) 
百度网盘提取码：6666 
<li>下载权重文件并放入checkpoint文件夹中，最终完成的目录应该是xx/model/checkpoint-xx  
  
测试版仅开放了0.4k的checkpoint  
下载地址
[百度网盘地址](链接：链接：https://pan.baidu.com/s/1nugDoRroD2I0dX3fcP9umA?pwd=6666) 百度网盘提取码：6666   
<li>运行python脚本  
``python demo.py``
##注意事项
<li>0.4k版本为测试版，训练数据极少，仅为测试使用，并且仅支持生成单技能，暂不支持生存多个技能连携的代码，同时生成的代码效果无法保证，如有需求请期待后续正式版本以及定制版本
<li>ai生成属不可控因素，生成的代码不保证100%有效，仍会出现bug、冗余代码或者出现额外的双引号等，仍然需要人工修改
<li>（重要）遵循ai规范，本ai模型仅用于学习交流使用，请勿用于不法用途以及商业用途，本人发布该模型初衷是希望大家更好的学习和交流，本ai模型涉及的所有相关信息公开，对于恶意使用本ai模型的本人无法也概不负责
##其他内容
如果相关问题，可以在github官方的issue中提出
##演示图片
![demo](./demo.png) 