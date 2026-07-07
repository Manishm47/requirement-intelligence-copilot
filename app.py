import streamlit as st

from services.llm_service import generate_ai_response
from prompts.prompts import (
    analyze_prompt,
    refine_prompt,
    delivery_pack_prompt
)


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Requirement Intelligence Copilot",
    page_icon="🚀",
    layout="wide"
)


# -----------------------------------
# Session State
# -----------------------------------

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "refine_done" not in st.session_state:
    st.session_state.refine_done = False

if "analysis_output" not in st.session_state:
    st.session_state.analysis_output = ""

if "refined_output" not in st.session_state:
    st.session_state.refined_output = ""

if "delivery_output" not in st.session_state:
    st.session_state.delivery_output = ""


# -----------------------------------
# Header
# -----------------------------------

st.title("🚀 Requirement Intelligence Copilot")

st.write(
    "Transform unclear requirements into development-ready SDLC artifacts"
)


# -----------------------------------
# Requirement Input
# -----------------------------------

requirement = st.text_area(
    "Paste Requirement / Meeting Transcript",
    height=250
)


st.divider()


# -----------------------------------
# Buttons
# -----------------------------------

col1, col2, col3 = st.columns(3)


# STEP 1 - ANALYSIS

with col1:

    analyze_clicked = st.button(
        "🔍 Analyze Requirement",
        disabled=False
    )


# STEP 2 - REFINEMENT

with col2:

    refine_clicked = st.button(
        "✨ Improve Requirement",
        disabled=not st.session_state.analysis_done
    )


# STEP 3 - DELIVERY PACK

with col3:

    delivery_clicked = st.button(
        "🚀 Generate Delivery Pack",
        disabled=not st.session_state.refine_done
    )



# -----------------------------------
# Process Actions
# -----------------------------------

if analyze_clicked:

    if requirement.strip():

        with st.spinner("Analyzing requirement..."):

            st.session_state.analysis_output = generate_ai_response(
                analyze_prompt(requirement)
            )

            st.session_state.analysis_done = True

    else:
        st.warning("Please enter requirement first")



if refine_clicked:

    with st.spinner("Improving requirement..."):

        st.session_state.refined_output = generate_ai_response(
            refine_prompt(requirement)
        )

        st.session_state.refine_done = True



if delivery_clicked:

    with st.spinner("Creating delivery artifacts..."):

        st.session_state.delivery_output = generate_ai_response(
            delivery_pack_prompt(
                st.session_state.refined_output
            )
        )


# -----------------------------------
# Display Output
# -----------------------------------

if st.session_state.analysis_output:

    st.divider()

    st.markdown("## 🔍 Requirement Analysis")

    st.markdown(
        st.session_state.analysis_output
    )



if st.session_state.refined_output:

    st.divider()

    st.markdown("## ✨ Refined Requirement")

    st.markdown(
        st.session_state.refined_output
    )



if st.session_state.delivery_output:

    st.divider()

    st.markdown("## 🚀 Delivery Pack")

    st.markdown(
        st.session_state.delivery_output
    )
