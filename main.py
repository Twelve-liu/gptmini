import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_response

st.title("GPTmini")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API Key：", type="password")
    st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的AI助手，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

human_input = st.chat_input()
if human_input:
    if not openai_api_key:
        st.write("请输入OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": human_input})
    st.chat_message("human").write(human_input)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_response(human_input, st.session_state["memory"], openai_api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)