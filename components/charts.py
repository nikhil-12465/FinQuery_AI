import plotly.graph_objects as go


def plot_stock_price(history):
    """
    Plot stock closing price
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=history.index,
            y=history["Close"],
            mode="lines",
            name="Close Price"
        )
    )

    fig.update_layout(
        title="Stock Price Trend",
        xaxis_title="Date",
        yaxis_title="Price ($)"
    )

    return fig


def plot_moving_average(history):
    """
    Plot stock price with moving average
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=history.index,
            y=history["Close"],
            mode="lines",
            name="Close Price"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=history.index,
            y=history["Moving_Average"],
            mode="lines",
            name="50 Day MA"
        )
    )

    fig.update_layout(
        title="Moving Average Analysis",
        xaxis_title="Date",
        yaxis_title="Price ($)"
    )

    return fig


def plot_revenue_trend(years, revenues):
    """
    Revenue chart
    """

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=years,
            y=revenues,
            name="Revenue"
        )
    )

    fig.update_layout(
        title="Revenue Trend",
        xaxis_title="Year",
        yaxis_title="Revenue"
    )

    return fig


def plot_cashflow_trend(years, cashflows):
    """
    Cash Flow chart
    """

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=years,
            y=cashflows,
            name="Cash Flow"
        )
    )

    fig.update_layout(
        title="Operating Cash Flow Trend",
        xaxis_title="Year",
        yaxis_title="Cash Flow"
    )

    return fig