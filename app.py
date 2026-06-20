import streamlit as st

from components.dashboard import (
    show_dashboard
)

from components.analyst import (
    show_analyst
)

from components.comparison import (
    show_comparison
)

from components.rag_chat import (
    show_rag_chat
)

st.set_page_config(
    page_title="FinQUERY_AI",
    page_icon="📈",
    layout="wide"
)
st.info(
    "Enter a company ticker and click Analyze to fetch live financial data."
)

st.markdown(
    """
    <h1 style="text-align:center;">
        📈 FinQUERY_AI
    </h1>

    <p style="text-align:center; font-size:20px;">
        AI-Powered Financial Analysis Platform
    </p>

    <p style="text-align:center;">
        📊 Financial Dashboard •
        🤖 AI Financial Analyst •
        ⚖️ Company Comparison •
        📄 Financial Report RAG
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Dashboard",
        "🤖 AI Analyst",
        "⚖️ Comparison",
        "📄 Financial Report RAG"
    ]
)

with tab1:
    show_dashboard()

with tab2:
    show_analyst()

with tab3:
    show_comparison()

with tab4:
    show_rag_chat()