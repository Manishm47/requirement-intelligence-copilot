import streamlit as st

from services.llm_service import generate_ai_response
from prompts.prompts import (
    analyze_prompt,
    refine_prompt,
    delivery_pack_prompt
)


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Requirement Intelligence Copilot",
    page_icon="🚀",
    layout="wide"
)


# -----------------------------
# Session State
# -----------------------------
if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "refined_requirement" not in st.session_state:
    st.session_state.refined_requirement = None

if "delivery_pack" not in st.session_state:
    st.session_state.delivery_pack = None


# -----------------------------
# Header
# -----------------------------
st.title("🚀 Requirement Intelligence Copilot")

st.write(
    "Transform unclear requirements into development-ready SDLC artifacts"
)


# -----------------------------
# Input
# -----------------------------
requirement = st.text_area(
    "Paste Requirement / Meeting Transcript",
    height=250
)


st.divider()


# -----------------------------
# Workflow Status
# -----------------------------
st.subheader("Requirement Intelligence Workflow")

col1, col2, col3 = st.columns(3)

with col1:
    if st.session_state.analysis:
        st.success("✅ Step 1 Completed")
    else:
        st.info("① Requirement Analysis")

with col2:
    if st.session_state.refined_requirement:
        st.success("✅ Step 2 Completed")
    else:
        st.info("② Requirement Enhancement")

with col3:
    if st.session_state.delivery_pack:
        st.success("✅ Step 3 Completed")
    else:
        st.info("③ SDLC Generation")


st.divider()


# -----------------------------
# Step Buttons
# -----------------------------
b1, b2, b3 = st.columns(3)


# STEP 1
with b1:

    if st.button(
        "🔍 Analyze & Find Gaps",
        use_container_width=True
    ):

        if requirement.strip():

            with st.spinner(
                "Analyzing requirement quality..."
            ):
                st.session_state.analysis = generate_ai_response(
                    analyze_prompt(requirement)
                )

        else:
            st.warning(
                "Please enter requirement first"
            )


# STEP 2
with b2:

    refine_disabled = (
        st.session_state.analysis is None
    )

    if st.button(
        "✨ Generate Improved Requirement",
        disabled=refine_disabled,
        use_container_width=True
    ):

        with st.spinner(
            "Improving requirement..."
        ):

            st.session_state.refined_requirement = generate_ai_response(
                refine_prompt(requirement)
            )


# STEP 3
with b3:

    delivery_disabled = (
        st.session_state.refined_requirement is None
    )

    if st.button(
        "🚀 Generate SDLC Artifacts",
        disabled=delivery_disabled,
        use_container_width=True
    ):

        with st.spinner(
            "Creating BRD, User Stories and Test Cases..."
        ):

            st.session_state.delivery_pack = generate_ai_response(
                delivery_pack_prompt(
                    st.session_state.refined_requirement
                )
            )


# -----------------------------
# Results
# -----------------------------

if st.session_state.analysis:

    st.divider()

    st.header("🔍 Requirement Intelligence Report")

    st.markdown(
        st.session_state.analysis
    )


if st.session_state.refined_requirement:

    st.divider()

    st.header("✨ Improved Requirement Specification")

    st.markdown(
        st.session_state.refined_requirement
    )


if st.session_state.delivery_pack:

    st.divider()

    st.header("🚀 SDLC Artifact Pack")

    st.markdown(
        st.session_state.delivery_pack
    )
