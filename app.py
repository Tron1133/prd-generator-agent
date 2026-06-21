import streamlit as st

from agent import (
    generate_prd,
    competitor_analysis
)

from pdf_generator import create_pdf


# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="PM Copilot",
    page_icon="📝",
    layout="wide"
)

# ==================================
# CUSTOM CSS
# ==================================

st.markdown(
    """
    <style>

    /* Remove excessive top padding */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    /* Full width buttons */
    .stButton button {
        width: 100%;
    }

    .stDownloadButton button {
        width: 100%;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ==================================
# HEADER
# ==================================

st.title("PM Copilot")

st.caption(
    "Generate Product Requirement Documents and Competitor Research using AI"
)

# ==================================
# LAYOUT
# ==================================

left_col, right_col = st.columns([0.8, 1.2])

# ==================================
# LEFT PANEL
# ==================================

with left_col:

    st.subheader("📝 Product Input")

    tool = st.selectbox(
        "Select Tool",
        [
            "PRD Generator",
            "Competitor Research"
        ]
    )

    product_description = st.text_area(
        "Describe your Product Idea",
        height=250,
        placeholder="""
Example:

A platform that helps college students discover campus events,
RSVP and receive personalized reminders.

OR

A fintech app that helps users automatically save money and
invest in mutual funds.
"""
    )

    generate_btn = st.button(
        "Generate",
        use_container_width=True
    )

# ==================================
# GENERATE
# ==================================

if generate_btn:

    if not product_description.strip():

        st.warning(
            "Please describe your product idea."
        )

    else:

        with st.spinner("Generating..."):

            try:

                if tool == "PRD Generator":

                    result = generate_prd(
                        product_description
                    )

                else:

                    result = competitor_analysis(
                        product_description
                    )

                st.session_state["result"] = result
                st.session_state["tool"] = tool

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

# ==================================
# RIGHT PANEL
# ==================================

with right_col:

    st.subheader("📄 Generated Output")

    if "result" in st.session_state:

        pdf = create_pdf(
            st.session_state["result"]
        )

        # Export button at top

        st.download_button(
            label="📥 Export PDF",
            data=pdf,
            file_name=f"{st.session_state['tool']}.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        st.divider()

        # Scrollable result container

        output_container = st.container(
            height=650,
            border=True
        )

        with output_container:

            st.markdown(
                st.session_state["result"]
            )

    else:

        output_container = st.container(
            height=650,
            border=True
        )

        with output_container:

            st.info(
                "Generated output will appear here."
            )