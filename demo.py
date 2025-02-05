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