from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
tokenizer = AutoTokenizer.from_pretrained("huskyhong/noname-ai-v2", trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained("huskyhong/noname-ai-v2", device_map="auto", trust_remote_code=True).eval() # 采用gpu加载模型
model = AutoModelForCausalLM.from_pretrained("huskyhong/noname-ai-v2", device_map="cpu", trust_remote_code=True).eval() # 采用cpu加载模型
model.generation_config = GenerationConfig.from_pretrained("huskyhong/noname-ai-v2", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参
# 第一代模型请将huskyhong/noname-ai-v2改为huskyhong/noname-ai-v1，轻量版模型请将huskyhong/noname-ai-v2改为huskyhong/noname-ai-v2-light

prompt = "请帮我编写一个技能，技能效果如下：" + input("请输入技能效果：")
response, history = model.chat(tokenizer, prompt, history = [])
print(response)

prompt = "请帮我编写一张卡牌，卡牌效果如下：：" + input("请输入卡牌效果：")
response, history = model.chat(tokenizer, prompt, history = [])
print(response)
