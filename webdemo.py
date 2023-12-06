from transformers import AutoModel, AutoTokenizer
import streamlit as st


st.set_page_config(
    page_title="无名杀AI",
    page_icon=":robot:",
    layout='wide'
)


@st.cache_resource
def get_model():
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from transformers.generation import GenerationConfig
    from peft import AutoPeftModelForCausalLM
    tokenizer = AutoTokenizer.from_pretrained("huskyhong/noname-ai-v1", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("huskyhong/noname-ai-v1", device_map="auto", trust_remote_code=True).eval() # 采用gpu加载模型
    # model = AutoModelForCausalLM.from_pretrained("huskyhong/noname-ai-v1", device_map="cpu", trust_remote_code=True).eval() # 采用cpu加载模型
    model.generation_config = GenerationConfig.from_pretrained("huskyhong/noname-ai-v1", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

    return tokenizer,model


tokenizer, model = get_model()

st.title("无名杀AI")

max_length = st.sidebar.slider(
    'max_length', 0, 32768, 8192, step=1
)
top_p = st.sidebar.slider(
    'top_p', 0.0, 1.0, 0.8, step=0.01
)
temperature = st.sidebar.slider(
    'temperature', 0.0, 1.0, 0.8, step=0.01
)

if 'history' not in st.session_state:
    st.session_state.history = []

if 'past_key_values' not in st.session_state:
    st.session_state.past_key_values = None

for i, (query, response) in enumerate(st.session_state.history):
    with st.chat_message(name="user", avatar="user"):
        st.markdown(query)
    with st.chat_message(name="assistant", avatar="assistant"):
        st.markdown(response)
with st.chat_message(name="user", avatar="user"):
    input_placeholder = st.empty()
with st.chat_message(name="assistant", avatar="assistant"):
    message_placeholder = st.empty()

prompt_text = st.text_area(label="输入技能效果",
                           height=100,
                           placeholder="请在这儿输入您想要的技能效果")

button = st.button("发送", key="predict")

if button:
    input_placeholder.markdown(prompt_text)
    history, past_key_values = st.session_state.history, st.session_state.past_key_values
    response, history = model.chat(tokenizer, "请帮我编写一个技能，技能效果如下：" + prompt_text, history = [])
    message_placeholder.markdown(response)

    st.session_state.history = history
    st.session_state.past_key_values = past_key_values
