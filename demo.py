import json
import os
# os.environ["CUDA_VISIBLE_DEVICES"] ="0"
def loadmodel(modelpath):
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from transformers.generation import GenerationConfig
    from peft import AutoPeftModelForCausalLM
    tokenizer = AutoTokenizer.from_pretrained(modelpath, trust_remote_code=True)
    # model = AutoModelForCausalLM.from_pretrained(modelpath, device_map="auto", trust_remote_code=True,use_flash_attn=False).eval()
    model = AutoPeftModelForCausalLM.from_pretrained(
        "./checkpoint/正式版v1.0", # path to the output directory
        device_map="auto",
        bf16=True,
        trust_remote_code=True,
        use_flash_attn=False
        ).eval()
    model.generation_config = GenerationConfig.from_pretrained(modelpath, trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

    return tokenizer,model
def llmchat(tokenizer,model,query,historys):
    response, history = model.chat(tokenizer, query, history = historys)
    return response,history

tokenizer,model = loadmodel("./models/QWen-7B-Chat")
while True:
    print("请输入技能效果：")
    prompt = input()
    prompt = "请帮我编写一个技能，技能效果如下：" + prompt
    history = []
    llmanswer,history = llmchat(tokenizer,model,prompt,history)
    print(llmanswer)

