import streamlit as st

from services.llm_service import generate_ai_response

from prompts.prompts import (
    analyze_prompt,
    refine_prompt,
    delivery_prompt
)


st.set_page_config(
    page_title="Requirement Intelligence Copilot",
    layout="wide"
)


st.title("🚀 Requirement Intelligence Copilot")

st.write(
    "Transform unclear requirements into development-ready SDLC artifacts"
)


# session memory

if "analysis" not in st.session_state:
    st.session_state.analysis = ""

if "refined" not in st.session_state:
    st.session_state.refined = ""

if "delivery" not in st.session_state:
    st.session_state.delivery = ""


requirement = st.text_area(
    "Paste Requirement / Meeting Transcript",
    height=250
)


col1, col2, col3 = st.columns(3)


with col1:

    if st.button("🔍 Analyze Requirement"):

        if requirement:

            with st.spinner("Analyzing requirement quality..."):

                st.session_state.analysis = generate_ai_response(
                    analyze_prompt(requirement)
                )


with col2:

    if st.button("✨ Refine Requirement"):

        if requirement:

            with st.spinner("Creating development ready requirement..."):

                st.session_state.refined = generate_ai_response(
                    refine_prompt(requirement)
                )


with col3:

    if st.button("🚀 Create Delivery Pack"):

        input_requirement = (
            st.session_state.refined
            if st.session_state.refined
            else requirement
        )

        if input_requirement:

            with st.spinner("Creating SDLC artifacts..."):

                st.session_state.delivery = generate_ai_response(
                    delivery_prompt(input_requirement)
                )


if st.session_state.analysis:

    st.divider()

    st.header("🔍 Requirement Analysis")

    st.markdown(
        st.session_state.analysis
    )


if st.session_state.refined:

    st.divider()

    st.header("✨ Refined Requirement")

    st.markdown(
        st.session_state.refined
    )


if st.session_state.delivery:

    st.divider()

    st.header("🚀 Delivery Pack")

    st.markdown(
        st.session_state.delivery
    )
