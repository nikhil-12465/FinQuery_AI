import streamlit as st

from services.financial_data import get_financial_metrics
from services.stock_data import (
    get_stock_history,
    get_current_stock_info,
    get_moving_average
)

from components.charts import (
    plot_stock_price,
    plot_moving_average
)

from utils.helpers import format_large_number


def show_dashboard():

    ticker = st.text_input(
        "Enter Company Ticker"
    )

    if not st.button("📊 Analyze Company"):
        return

    if not ticker:
        st.warning(
            "Please enter a ticker."
        )
        return

    try:

        # -------------------
        # Financial Metrics
        # -------------------

        financial_data = get_financial_metrics(ticker)

        stock_info = get_current_stock_info(ticker)

        st.subheader("📈 Key Financial Metrics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Market Cap",
                format_large_number(
                    financial_data["market_cap"]
                )
            )

        with col2:
            st.metric(
                "Revenue",
                format_large_number(
                    financial_data["revenue"]
                )
            )

        with col3:
            st.metric(
                "Net Income",
                format_large_number(
                    financial_data["net_income"]
                )
            )

        with col4:
            st.metric(
                "Operating Cash Flow",
                format_large_number(
                    financial_data["operating_cashflow"]
                )
            )

        st.divider()

        # -------------------
        # Stock Metrics
        # -------------------

        st.subheader("📉 Market Information")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Current Price",
                stock_info["current_price"]
            )

        with col2:
            st.metric(
                "Day High",
                stock_info["day_high"]
            )

        with col3:
            st.metric(
                "52W High",
                stock_info["fifty_two_week_high"]
            )

        with col4:
            st.metric(
                "Volume",
                format_large_number(
                    stock_info["volume"]
                )
            )

        st.divider()

        # -------------------
        # Stock Charts
        # -------------------

        history = get_stock_history(
            ticker,
            period="1y"
        )

        history = get_moving_average(
            history
        )

        st.subheader("📈 Stock Price Trend")

        stock_chart = plot_stock_price(
            history
        )

        st.plotly_chart(
            stock_chart,
            use_container_width=True
        )

        st.subheader("📉 Moving Average Analysis")

        ma_chart = plot_moving_average(
            history
        )

        st.plotly_chart(
            ma_chart,
            use_container_width=True
        )

        st.divider()

        # -------------------
        # Company Overview
        # -------------------

        st.subheader("🏢 Company Overview")

        col1, col2 = st.columns(2)

        with col1:
            st.write(
                f"**Company:** {financial_data['company_name']}"
            )

            st.write(
                f"**Sector:** {financial_data['sector']}"
            )

        with col2:
            st.write(
                f"**Industry:** {financial_data['industry']}"
            )

            st.write(
                f"**P/E Ratio:** {financial_data['pe_ratio']}"
            )

    except Exception as e:

        st.error(
            f"Dashboard Error: {e}"
        )