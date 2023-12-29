from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import streamlit as st

st.set_page_config(
    page_title="无名杀AI",
    page_icon=":robot:",
    layout='wide'
)

@st.cache_resource
def get_model():
    tokenizer = AutoTokenizer.from_pretrained("./models", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("./models", device_map="cpu", trust_remote_code=True).float()
    model.generation_config = GenerationConfig.from_pretrained("./models", trust_remote_code=True)
    return tokenizer, model

tokenizer, model = get_model()

st.title("无名杀AI")

if 'history' not in st.session_state:
    st.session_state.history = []

if 'past_key_values' not in st.session_state:
    st.session_state.past_key_values = None

# Function to display a chat message
def display_message(name, avatar, content):
    with st.chat_message(name=name, avatar=avatar):
        st.markdown(content)

# Display chat history
for i, (query, response) in enumerate(st.session_state.history):
    display_message("user", "user", query)
    display_message("assistant", "assistant", response)

# User input and assistant response placeholders
input_placeholder = st.empty()
message_placeholder = st.empty()

# Text area for input
prompt_text = st.text_area(label="输入技能效果", height=100, placeholder="请在这儿输入您想要的技能效果")

# Generate Skill or Card Button
if st.button("生成技能", key="predict_skill") or st.button("生成卡牌", key="predict_card"):
    input_text = "请帮我编写一个技能，技能效果如下：" + prompt_text if "predict_skill" in st.session_state else "请帮我编写一张卡牌，技能效果如下：" + prompt_text
    input_placeholder.markdown(prompt_text)

    # Stream generation
    history, past_key_values = [], st.session_state.past_key_values
    for response in model.chat_stream(tokenizer, input_text, history=[]):

        message_placeholder.markdown(response)
        st.session_state.history = history
        st.session_state.past_key_values = past_key_values
    display_message("user", "user", prompt_text)
    display_message("assistant", "assistant", response)
