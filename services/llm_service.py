
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def initialize_llm():

    groq_api_key = os.getenv(
        "GROQ_API_KEY"
    )

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=groq_api_key
    )

    return llm


def generate_financial_analysis(company_data):
    """
    AI Financial Analyst
    """

    llm = initialize_llm()

    def to_billions(value):
        try:
            return f"${float(value)/1_000_000_000:.2f} Billion"
        except:
            return "N/A"

    prompt = f"""
You are a senior Wall Street financial analyst.

Analyze the company using the financial data provided below.

Company Information:
--------------------
Company Name: {company_data['company_name']}
Sector: {company_data['sector']}
Industry: {company_data['industry']}

Financial Metrics:
--------------------
Market Capitalization: {to_billions(company_data['market_cap'])}
Revenue (FY Latest): {to_billions(company_data['revenue'])}
Net Income (FY Latest): {to_billions(company_data['net_income'])}
Operating Income (FY Latest): {to_billions(company_data['operating_income'])}
Operating Cash Flow: {to_billions(company_data['operating_cashflow'])}

EPS: {company_data['eps']}
Profit Margin: {company_data['profit_margin']}
PE Ratio: {company_data['pe_ratio']}

Instructions:
--------------------
1. Use all provided financial metrics.
2. Mention actual revenue, net income and cash flow values.
3. Evaluate profitability.
4. Evaluate operational efficiency.
5. Evaluate financial strength.
6. Mention potential risks.
7. Mention growth opportunities.
8. Give an investment outlook.
9. Provide a final verdict.

IMPORTANT:
The revenue, net income and operating income values are provided above.
Do not state that these values are unavailable.
Use the exact values in your analysis.

Format your response using the following sections:

## Company Overview
## Financial Health
## Strengths
## Risks
## Growth Opportunities
## Investment Outlook
## Final Verdict
"""

    response = llm.invoke(prompt)

    return response.content