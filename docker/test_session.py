import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

# On top
cookies = EncryptedCookieManager(
    prefix="myapp/",
    password=os.environ.get("COOKIES_PASSWORD", "SuperSecretPassword!")
)

if not cookies.ready():
    st.stop()

# Caching resource example (for heavier data loads)
@st.cache_data  # or @st.cache_resource for resources like DB connections
def expensive_setup():
    # e.g. load credentials or initialize DB
    return {"foo": "bar"}

data = expensive_setup()
