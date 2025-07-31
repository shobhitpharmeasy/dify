import streamlit as st
import time

user_input = "SELECT * FROM patients WHERE blood_pressure > 140"  # Example input

with st.expander("Processing your query..."):
    spinner_message = f"Processing your query: {(str(user_input[:50]) + '...') if len(user_input) > 50 else user_input}"

    with st.spinner(spinner_message):
        st.success("fuck")
        time.sleep(3)  # Simulate processing
        st.success("Query processed successfully!")
