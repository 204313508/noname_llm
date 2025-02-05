import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
import torch
from threading import Thread
import time

# 设置页面配置
st.set_page_config(
    page_title="无名杀AI v3.0 在线版- by AKA臭脸羊驼",
    page_icon="🐐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 模型加载函数
@st.cache_resource
def load_model():
    try:
        with st.spinner("🦙 正在加载模型，首次加载可能需要较长时间..."):
            model = AutoModelForCausalLM.from_pretrained(
                "huskyhong/noname-ai-v3.0",
                torch_dtype="auto",
                device_map="auto"
            )
            tokenizer = AutoTokenizer.from_pretrained("./models")
        return model, tokenizer
    except Exception as e:
        st.error(f"❌ 模型加载失败：{str(e)}")
        st.stop()

# 加载模型
model, tokenizer = load_model()

# 侧边栏
with st.sidebar:
    st.title("💖 支持开发者")
    try:
        st.image("赞赏码.jpg", 
                caption="您的支持是我更新的动力", 
                use_container_width=True)
    except FileNotFoundError:
        st.warning("找不到赞赏码图片")

# 主界面
st.title("🎮 无名杀AI v3.0 -网页端")

st.markdown("---")

# 初始化会话状态
if "generating" not in st.session_state:
    st.session_state.update({
        "generating": False,
        "first_token_received": False
    })

# 模式选择
mode = st.radio("请选择生成模式：", ["技能生成", "卡牌生成"], horizontal=True)
prompt_map = {
    "技能生成": "请帮我用JavaScript编写一个无名杀游戏的技能，技能效果如下：",
    "卡牌生成": "请帮我用JavaScript编写一张无名杀游戏的卡牌，卡牌效果如下："
}

# 输入区域
effect_desc = st.text_area(
    "✍️ 效果描述：",
    height=100,
    placeholder="请输入想要实现的技能/卡牌效果描述..."
)

# 生成按钮
if st.button("🚀 开始生成", use_container_width=True):
    if not effect_desc.strip():
        st.warning("⚠️ 请输入效果描述！")
        st.stop()
    
    # 重置状态
    st.session_state.update({
        "generating": True,
        "first_token_received": False
    })
    
    # 构建提示词
    prompt = prompt_map[mode] + effect_desc.strip()
    
    messages = [
        {"role": "system", "content": "你是由B站up主AKA臭脸臭羊驼训练得到的无名杀AI，旨在帮助用户编写无名杀技能或卡牌代码"},
        {"role": "user", "content": prompt}
    ]
    
    # 准备生成参数
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

    # 状态初始化
    status_area = st.empty()
    code_output = st.empty()
    full_response = ""
    start_time = time.time()

    # 启动生成线程
    def generate():
        try:
            model.generate(**model_inputs, streamer=streamer, max_new_tokens=8192)
        except Exception as e:
            st.error(f"❌ 生成错误：{str(e)}")
        finally:
            st.session_state.generating = False

    thread = Thread(target=generate)
    thread.start()

    # 实时状态处理
    while st.session_state.generating:
        # 显示初始等待提示
        if not st.session_state.first_token_received:
            elapsed_time = time.time() - start_time
            status_message = f"""
            🕒 正在努力生成中... ({elapsed_time:.1f}s)
            ![正在加载](https://i.gifer.com/ZZ5H.gif)
            ⏳ 模型初始化可能需要较长时间，请耐心等待
            """
            status_area.markdown(status_message, unsafe_allow_html=True)
        
        # 尝试获取流式输出
        try:
            for token in streamer:
                # 收到第一个token时清除等待提示
                if not st.session_state.first_token_received:
                    status_area.empty()
                    st.session_state.first_token_received = True
                
                full_response += token
                code_output.code(full_response)
                break  # 逐个token处理
        except StopIteration:
            break
        
        time.sleep(1)

    # 最终处理
    status_area.empty()
    if full_response:
        st.success("✅ 生成完成！")
        st.download_button(
            label="📥 下载代码",
            data=full_response,
            file_name="generated_code.js",
            mime="text/javascript",
            use_container_width=True
        )
    else:
        st.warning("⚠️ 未能生成有效内容，请尝试调整输入描述")