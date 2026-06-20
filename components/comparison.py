import streamlit as st
import pandas as pd
import plotly.express as px

from services.financial_data import get_financial_metrics


def safe_float(value):

    try:
        return float(value)
    except:
        return 0


def format_money(value):

    try:

        if value in [None, "", "N/A"]:
            return "N/A"

        value = float(value)

        if value >= 1_000_000_000_000:
            return f"${value/1_000_000_000_000:.2f} T"

        elif value >= 1_000_000_000:
            return f"${value/1_000_000_000:.2f} B"

        elif value >= 1_000_000:
            return f"${value/1_000_000:.2f} M"

        return f"${value:,.0f}"

    except:
        return "N/A"


def show_comparison():

    st.header("⚖️ Company Comparison")

    col1, col2 = st.columns(2)

    with col1:

       ticker1 = st.text_input(
            "First Company"
        )

    with col2:

       ticker2 = st.text_input(
            "Second Company"
        )

    if st.button("Compare Companies"):
        if not ticker1 or not ticker2:
            st.warning(
                "Please enter both tickers."
            )
            return

        with st.spinner(
            "Fetching financial data..."
        ):

            company1 = get_financial_metrics(
                ticker1.upper()
            )

            company2 = get_financial_metrics(
                ticker2.upper()
            )

        st.success(
            f"{company1['company_name']} vs {company2['company_name']}"
        )

        comparison_df = pd.DataFrame({

            "Metric": [

                "Market Cap",
                "Revenue",
                "Net Income",
                "Operating Income",
                "Operating Cash Flow",
                "PE Ratio",
                "Profit Margin",
                "Dividend Yield",
                "Book Value",
                "ROE"

            ],

            company1["company_name"]: [

                format_money(
                    company1["market_cap"]
                ),

                format_money(
                    company1["revenue"]
                ),

                format_money(
                    company1["net_income"]
                ),

                format_money(
                    company1["operating_income"]
                ),

                format_money(
                    company1["operating_cashflow"]
                ),

                company1["pe_ratio"],
                company1["profit_margin"],
                company1["dividend_yield"],
                company1["book_value"],
                company1["roe"]

            ],

            company2["company_name"]: [

                format_money(
                    company2["market_cap"]
                ),

                format_money(
                    company2["revenue"]
                ),

                format_money(
                    company2["net_income"]
                ),

                format_money(
                    company2["operating_income"]
                ),

                format_money(
                    company2["operating_cashflow"]
                ),

                company2["pe_ratio"],
                company2["profit_margin"],
                company2["dividend_yield"],
                company2["book_value"],
                company2["roe"]

            ]
        })

        st.subheader(
            "📊 Financial Comparison"
        )

        st.dataframe(
            comparison_df,
            use_container_width=True
        )

        st.divider()

        # Revenue Chart

        st.subheader(
            "📈 Revenue Comparison"
        )

        revenue_chart = px.bar(

            x=[
                company1["company_name"],
                company2["company_name"]
            ],

            y=[
                safe_float(
                    company1["revenue"]
                ),

                safe_float(
                    company2["revenue"]
                )
            ],

            labels={
                "x": "Company",
                "y": "Revenue"
            },

            title="Revenue Comparison"
        )

        st.plotly_chart(
            revenue_chart,
            use_container_width=True
        )

        st.divider()

        # Net Income Chart

        st.subheader(
            "💰 Net Income Comparison"
        )

        income_chart = px.bar(

            x=[
                company1["company_name"],
                company2["company_name"]
            ],

            y=[
                safe_float(
                    company1["net_income"]
                ),

                safe_float(
                    company2["net_income"]
                )
            ],

            labels={
                "x": "Company",
                "y": "Net Income"
            },

            title="Net Income Comparison"
        )

        st.plotly_chart(
            income_chart,
            use_container_width=True
        )

        st.divider()

        # Conclusion

        st.subheader(
            "🏆 Quick Conclusion"
        )

        market_cap_1 = safe_float(
            company1["market_cap"]
        )

        market_cap_2 = safe_float(
            company2["market_cap"]
        )

        revenue_1 = safe_float(
            company1["revenue"]
        )

        revenue_2 = safe_float(
            company2["revenue"]
        )

        net_income_1 = safe_float(
            company1["net_income"]
        )

        net_income_2 = safe_float(
            company2["net_income"]
        )

        larger_company = (
            company1["company_name"]
            if market_cap_1 > market_cap_2
            else company2["company_name"]
        )

        higher_revenue = (
            company1["company_name"]
            if revenue_1 > revenue_2
            else company2["company_name"]
        )

        more_profitable = (
            company1["company_name"]
            if net_income_1 > net_income_2
            else company2["company_name"]
        )

        st.info(
            f"""
📌 Larger Company: {larger_company}

📌 Higher Revenue: {higher_revenue}

📌 More Profitable: {more_profitable}
"""
        )