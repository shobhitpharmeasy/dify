import streamlit as st

# Read params
params = st.query_params
page = int(params.get("page", ["1"])[0])
q = params.get("q", [""])[0]

# Display inputs
new_page = st.number_input("Page", min_value=1, value=page)
new_q = st.text_input("Search", value=q)

# Update URL when changed
if new_page != page or new_q != q:
    st.query_params.clear()
    st.query_params.update({
        "page": str(new_page),
        "q": new_q
    })

st.write(f"Showing page {new_page}, filter: {new_q}")
