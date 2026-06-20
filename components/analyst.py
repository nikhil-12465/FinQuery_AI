import streamlit as st

from services.financial_data import get_financial_metrics
from services.llm_service import generate_financial_analysis


def show_analyst():

    st.header("🤖 AI Financial Analyst")

    ticker = st.text_input(
        "Enter Company Ticker",
        key="analyst_ticker"
    )

    if st.button("Generate Analysis"):

        with st.spinner("Analyzing company..."):
            if not ticker:
                st.warning(
                    "Please enter a ticker."
                )
                return

            company_data = get_financial_metrics(
                ticker.upper()
            )

            analysis = generate_financial_analysis(
                company_data
            )

        st.markdown("---")

        st.markdown(analysis)