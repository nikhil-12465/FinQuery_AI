import yfinance as yf
import streamlit as st

@st.cache_data(ttl=3600)
def get_financial_metrics(ticker):
    """
    Fetch company financial metrics using yfinance
    """

    try:

        stock = yf.Ticker(ticker)

        info = stock.info

        financials = stock.financials

        cashflow = stock.cashflow

        revenue = "N/A"
        net_income = "N/A"
        operating_income = "N/A"
        operating_cashflow = "N/A"

        try:

            if not financials.empty:

                if "Total Revenue" in financials.index:
                    revenue = financials.loc[
                        "Total Revenue"
                    ].iloc[0]

                if "Net Income" in financials.index:
                    net_income = financials.loc[
                        "Net Income"
                    ].iloc[0]

                if "Operating Income" in financials.index:
                    operating_income = financials.loc[
                        "Operating Income"
                    ].iloc[0]

        except:
            pass

        try:

            if not cashflow.empty:

                if "Operating Cash Flow" in cashflow.index:

                    operating_cashflow = cashflow.loc[
                        "Operating Cash Flow"
                    ].iloc[0]

        except:
            pass

        profit_margin = info.get(
            "profitMargins",
            "N/A"
        )

        try:
            profit_margin = (
                f"{profit_margin * 100:.2f}%"
            )
        except:
            profit_margin = "N/A"

        return {

            "company_name":
            info.get(
                "longName",
                "N/A"
            ),

            "sector":
            info.get(
                "sector",
                "N/A"
            ),

            "industry":
            info.get(
                "industry",
                "N/A"
            ),

            "market_cap":
            info.get(
                "marketCap",
                "N/A"
            ),

            "pe_ratio":
            info.get(
                "trailingPE",
                "N/A"
            ),

            "eps":
            info.get(
                "trailingEps",
                "N/A"
            ),

            "profit_margin":
            profit_margin,

            "revenue": clean_number(revenue),

            "net_income": clean_number(net_income),

            "operating_income": clean_number(operating_income),
            
            "operating_cashflow": clean_number(operating_cashflow),

            "dividend_yield":
            info.get(
                "dividendYield",
                "N/A"
            ),

            "book_value":
            info.get(
                "bookValue",
                "N/A"
            ),

            "roe":
            info.get(
                "returnOnEquity",
                "N/A"
            )
        }

    except Exception as e:

        return {

            "company_name": "N/A",
            "sector": "N/A",
            "industry": "N/A",
            "market_cap": "N/A",
            "pe_ratio": "N/A",
            "eps": "N/A",
            "profit_margin": "N/A",
            "revenue": "N/A",
            "net_income": "N/A",
            "operating_income": "N/A",
            "operating_cashflow": "N/A",
            "dividend_yield": "N/A",
            "book_value": "N/A",
            "roe": "N/A"
        }
    
def clean_number(value):

    try:
        return float(value)
    except:
        return value