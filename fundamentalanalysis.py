import FundamentalAnalysis as fa
import pandas as pd
import os
import streamlit as st
from datetime import date
import datetime as dt
import pandas_datareader.data as web
from dateutil.relativedelta import relativedelta


st.set_page_config(layout="wide")
col1, col2 = st.beta_columns(2)

st.header('Stock Analysis')
st.subheader('Enter a ticker (uppercase)')

ticker = col1.text_input("Ticker", 'AAPL')
api = "f684dcaa18d79b3692c1feeea9b19f7a"

today = date.today()
start = dt.datetime(2015,1,1)
end = today
prices = web.DataReader(ticker, 'yahoo', start, end)
prices = prices["Adj Close"]


profile = fa.profile(ticker, api)
info_df = pd.DataFrame(profile)
df = info_df.head(10)

enterpriseValue = fa.enterprise(ticker, api)
ratings = fa.rating(ticker, api)
dcfAnnual = fa.discounted_cash_flow(ticker, api, period="annual")
# # # # # # Financial Statements # # # # # # #
balanceSheetAnnual = fa.balance_sheet_statement(ticker, api, period="annual")
incomeStatementAnnual = fa.income_statement(ticker, api, period="annual")
cashFlowAnnual = fa.cash_flow_statement(ticker, api, period="annual")
financialRatiosAnnual = fa.financial_ratios(ticker, api, period="annual")
growthAnnual = fa.financial_statement_growth(ticker, api, period="annual")

##DOWNLOAD BUTTON##
if st.button("Download Data"):
    writer = pd.ExcelWriter('Fundamental_Analysis{}.xlsx'.format(ticker), engine='xlsxwriter')

    profile.to_excel(writer, sheet_name="profile")
    enterpriseValue.to_excel(writer, sheet_name="EV")
    ratings.to_excel(writer, sheet_name="ratings")
    dcfAnnual.to_excel(writer, sheet_name="DCF")
    balanceSheetAnnual.to_excel(writer, sheet_name="balance sheet")
    incomeStatementAnnual.to_excel(writer, sheet_name="income statement")
    cashFlowAnnual.to_excel(writer, sheet_name="cash flow statement")
    financialRatiosAnnual.to_excel(writer, sheet_name="financial ratios")
    growthAnnual.to_excel(writer, sheet_name="growth rates")

    writer.save()


##OUTPUT##

col1.write('Company Profile')
col1.table(df)

col1.write('Enterprise Value')
col1.dataframe(enterpriseValue)

col1.write('Analyst Ratings')
col1.dataframe(ratings)

col1.write('DCF Model')
col1.dataframe(dcfAnnual)

col1.write('Balance Sheet')
col1.dataframe(balanceSheetAnnual)

col1.write('Income Statement')
col1.dataframe(incomeStatementAnnual)

col1.write('Cash Flow Statement')
col1.dataframe(cashFlowAnnual)

col1.write('Financial Ratios')
col1.dataframe(financialRatiosAnnual)

col1.write('Annual Growth Rates')
col1.dataframe(growthAnnual)

##Price Chart##
col2.write('Price Chart')
period = col2.selectbox('Period', ["3 M","1 Y", "3 Y"])

if period == "3 M":
    start = today - relativedelta(months=+3)
    end = today
    prices = web.DataReader(ticker, 'yahoo', start, end)
    prices = prices["Adj Close"]
    col2.line_chart(prices)
elif period == "1 Y":
    start = today - relativedelta(years=+1)
    end = today
    prices = web.DataReader(ticker, 'yahoo', start, end)
    prices = prices["Adj Close"]
    col2.line_chart(prices)
else :
    start = today - relativedelta(years=+3)
    end = today
    prices = web.DataReader(ticker, 'yahoo', start, end)
    prices = prices["Adj Close"]
    col2.line_chart(prices)
