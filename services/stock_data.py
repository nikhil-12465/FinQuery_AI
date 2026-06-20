import yfinance as yf
import pandas as pd
import streamlit as st


@st.cache_data(ttl=3600)
def get_stock_history(ticker, period="1y"):
    """
    Fetch historical stock prices

    Examples:
    period="1mo"
    period="3mo"
    period="6mo"
    period="1y"
    period="5y"
    """

    stock = yf.Ticker(ticker)

    history = stock.history(period=period)

    return history

@st.cache_data(ttl=3600)
def get_current_stock_info(ticker):
    """
    Fetch current stock information
    """

    stock = yf.Ticker(ticker)

    info = stock.info

    return {
        "current_price": info.get("currentPrice", "N/A"),
        "day_high": info.get("dayHigh", "N/A"),
        "day_low": info.get("dayLow", "N/A"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow", "N/A"),
        "volume": info.get("volume", "N/A")
    }


def get_moving_average(history, window=50):
    """
    Calculate moving average
    """

    history["Moving_Average"] = (
        history["Close"]
        .rolling(window=window)
        .mean()
    )

    return history