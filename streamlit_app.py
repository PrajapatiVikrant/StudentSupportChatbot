import streamlit as st
import time
from chatbot import ask_chatbot

# ---------------- PAGE ---------------- #

st.set_page_config(
    page_title="Student Support AI",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#2563EB;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🎓 Student Support AI")

    st.success("NLP + FAISS + Gemini")

    st.divider()

  

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- HEADER ---------------- #

st.markdown(
    "<div class='title'>🎓 Student Support AI Chatbot</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Ask anything related to Fees, Hostel, Library, Attendance and Scholarship.</div>",
    unsafe_allow_html=True
)

# ---------------- SHOW HISTORY ---------------- #

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- INPUT ---------------- #

prompt = st.chat_input("Type your question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            time.sleep(0.3)

            try:

                response = ask_chatbot(prompt)

            except Exception as e:

                response = f"❌ Error:\n\n{e}"

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )