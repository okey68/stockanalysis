import FundamentalAnalysis as fa
import pandas as pd
import os
import streamlit as st


ticker = st.text_input("Ticker", 'AAPL')
api = "f684dcaa18d79b3692c1feeea9b19f7a"

profile = fa.profile(ticker, api)
enterpriseValue = fa.enterprise(ticker, api)
ratings = fa.rating(ticker, api)
dcfAnnual = fa.discounted_cash_flow(ticker, api, period="annual")
# # # # # # Financial Statements # # # # # # #
balanceSheetAnnual = fa.balance_sheet_statement(ticker, api, period="annual")
incomeStatementAnnual = fa.income_statement(ticker, api, period="annual")
cashFlowAnnual = fa.cash_flow_statement(ticker, api, period="annual")
financialRatiosAnnual = fa.financial_ratios(ticker, api, period="annual")
growthAnnual = fa.financial_statement_growth(ticker, api, period="annual")

##OUTPUT##
st.write('Company Profile')
st.dataframe(profile)

st.write('Enterprise Value')
st.dataframe(enterpriseValue)

st.write('Analyst Ratings')
st.dataframe(ratings)

st.write('DCF Model')
st.dataframe(dcfAnnual)

st.write('Balance Sheet')
st.dataframe(balanceSheetAnnual)

st.write('Income Statement')
st.dataframe(incomeStatementAnnual)

st.write('Cash Flow Statement')
st.dataframe(cashFlowAnnual)

st.write('Financial Ratios')
st.dataframe(financialRatiosAnnual)

st.write('Annual Growth Rates')
st.dataframe(growthAnnual)