import streamlit as st
from agent import generate_prd

st.title("📄 PRD Generator AI Agent")

product_name = st.text_input(
    "Product Name"
)

problem_statement = st.text_area(
    "Problem Statement"
)

target_users = st.text_input(
    "Target Users"
)

features = st.text_area(
    "Key Features"
)

if st.button("Generate PRD"):

    with st.spinner("Generating PRD..."):

        prd = generate_prd(
            product_name,
            problem_statement,
            target_users,
            features
        )

        st.markdown(prd)