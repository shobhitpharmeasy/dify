import streamlit as st

with st.expander("Upload file"):
    uploaded = st.file_uploader("Choose file", label_visibility="visible")


import streamlit as st

prompt = st.chat_input(
    "Say something and/or attach a file",
    accept_file=True,  # Enable single file attachment
    file_type=["csv", "txt"],  # Optional: restrict file types
)

if prompt:
    if prompt.text:
        st.write("📝 You said:", prompt.text)
    if prompt["files"]:
        for file in prompt["files"]:
            st.write("📎 Uploaded file:", file.name)
