import pandas as pd
import streamlit as st

st.title("CSV File Upload — No Hashing")

# State flag to detect new file upload
st.session_state.setdefault("file_changed", False)

# Callback when user submits via chat_input
def on_submit():
    st.session_state["file_changed"] = True

# Chat input for file upload + optional text
uploaded_input = st.chat_input(
    "Upload a CSV or type a message",
    accept_file=True,
    file_type=["csv", "txt"],
    key="file_upload",
    on_submit=on_submit,
)

i = 0
print(i, uploaded_input)
i += 1

# Dummy widget to allow UI interaction and reruns
st.checkbox("Simulate UI interaction")

# Process only when new input is submitted
if uploaded_input:
    if st.session_state["file_changed"]:
        user_text = uploaded_input.text
        uploaded_files = uploaded_input.files

        if user_text:
            st.write("**User text input:**", user_text)

        for uploaded_file in uploaded_files:
            st.write(f"**Uploaded file name:** {uploaded_file.name}")
            try:
                df = pd.read_csv(uploaded_file)
                st.success("✅ New file uploaded and processed!")
                st.dataframe(df.head())
            except Exception as e:
                uploaded_file.seek(0)
                content = uploaded_file.read().decode("utf-8", errors="ignore")
                st.error(f"❌ Failed to read CSV: {e}")
                st.code(content[:500])
        st.session_state["file_changed"] = False
    else:
        st.info("⚠️ Same file — skipping processing.")
