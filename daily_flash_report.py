#cd C:\Users\HP\Desktop\PROGETTI\Econ-o-Mix\Daily Report
#streamlit run Daily-Mix.py

import streamlit as st
from streamlit_lottie import st_lottie
import requests
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader.data as web
import pandas_datareader.data as reader
import datetime
from datetime import date, timedelta

st.set_page_config(page_title="Daily Flash Report", page_icon=":chart_with_upwards_trend", layout="wide")

with st.container():
    st.subheader("Hi, I am Alessandro De Petra")
    st.title("Here you can find a brief (and I hope useful) tool for creating a report on the latest financial market data!")
    st.write("[Curious about me? Learn more >](https://www.linkedin.com/in/alessandro-de-petra-4b1a20141/)")

with st.container():
    st.write("----")
    st.header("Introduction to the Daily Flash Report")
    st.write("""
    - Part 1: Daily Return of the major Stock Market Indexes;
    - Part 2: Top 10 Best and Worst Performers of the S&P 500, Nasdaq 100 e Eurostoxx 50 (according to the latest daily stock return);
    - Part 3: Some Charts for visualizing Central Banks Policy Rates and Sovereign 10 Year Bond Yield;
    - Part 4: Daily Returns of the main Commodities and FX.
    """)
        
# Sidebar widgets
st.sidebar.header("Input Data")
st.sidebar.write("Select your desired analysis date:")
analysis_date = st.sidebar.selectbox("Choose from", [" ", "Last Trading Day", "Customized Dates"])
if analysis_date=="Last Trading Day":
    days = st.sidebar.number_input("Enter your Time Horizon in Days:", min_value=0, max_value=3000, value=1000)
    #days = 2000 #almost 5 years before today
    end_date = date.today()
    start_date = end_date-timedelta(days=days)
elif analysis_date=="Customized Dates":
    end_date = st.sidebar.text_input("Enter the Day of the Analysis (AAAA-MM-DD):")
    st.sidebar.write("You selected:", end_date)
    start_date = st.sidebar.text_input("Enter the Day from which you want to Analyze Data (AAAA-MM-DD):")
    st.sidebar.write("You selected:", start_date)
else: 
    st.sidebar.write(" ")

    # Title of the app
st.title("Your Daily Report-Mix")
st.header("Part 1: Daily Return of the major Stock Market Indexes")

# Text input for a user's name

general_index = ["^GSPC", "^IXIC", "^DJI", "^STOXX50E", "^STOXX", "FTSEMIB.MI", "^GDAXI", "^N225",  "^HSI", "SWDA.MI", "^FCHI"]
index_name = ["S&P 500","Nasdaq 100","Dow Jones", "Eurostoxx 50", "Eurostoxx 600", "Ftse Mib 30", "Cac 40", "Dax 30", "Hang Seng", "Nikkei 225", "MSCI World"]

index_data = yf.download(general_index, start=start_date, end=end_date)
index_data = index_data["Adj Close"]
index_data.index = index_data.index.strftime('%Y-%m-%d')

index_data_ret = index_data.pct_change()*100
index_data_ret = index_data_ret.dropna()
index_data_ret = round(index_data_ret, 3)
last_index_ret = index_data_ret.tail(5)
last_index_ret = last_index_ret.applymap(lambda x: '{:.4f}'.format(x))
last_index_ret = last_index_ret.astype(float)
last_index_ret = last_index_ret.applymap(lambda x: f"{x}%" if pd.notnull(x) else x)
last_index_ret = last_index_ret[["^GSPC", "^IXIC", "^DJI", "^STOXX50E", "^STOXX", "FTSEMIB.MI", "^FCHI", "^GDAXI", "^HSI", "^N225", "SWDA.MI"]]

fig, ax = plt.subplots(figsize=(10, 11))  # Imposta la dimensione della figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=last_index_ret.values, colLabels=index_name, rowLabels=last_index_ret.index, cellLoc='center', loc='center')
table.scale(3, 5)  # Aumenta larghezza e altezza delle celle
table.set_fontsize(22)

# Color the header
for i in range(len(general_index)):
    table[0,i].set_text_props(color="white", weight="bold")
    table[0,i].set_facecolor("#000080")  # Set background color for the header

for i in range(len(general_index)):
    table[5,i].set_facecolor("#FFFFE0")  # Set background color for the header
    
plt.show()

st.pyplot(fig)


#stock market indexes graphs
fig, axs = plt.subplots(2,2, figsize=(30, 15))
#usa
axs[0,0].plot(index_data_ret["^GSPC"], color = "blue")
axs[0,0].set_title(f'S&P 500 Last Close', fontsize=20)
axs[0,1].plot(index_data_ret["^DJI"], color = "blue")
axs[0,1].set_title(f'Dow Jones Last Close', fontsize=20)
axs[1,0].plot(index_data_ret["^IXIC"], color = "blue")
axs[1,0].set_title(f'Nasdaq Last Close', fontsize=20)
axs[1,1].plot(index_data_ret["^VIX"], color = "blue")
axs[1,1].set_title(f'Vix S&P Last Close', fontsize=20)

plt.show()
st.pyplot(fig)

fig, axs = plt.subplots(2,2, figsize=(30, 15))
#EU
axs[0,0].plot(index_data_ret["^STOXX50E"], color = "green")
axs[0,0].set_title(f'Eurostoxx 50 Last Close', fontsize=20)
axs[0,1].plot(index_data_ret["FTSEMIB.MI"], color = "green")
axs[0,1].set_title(f'Ftse Mib Last Close', fontsize=20)
axs[1,0].plot(index_data_ret["^GDAXI"], color = "green")
axs[1,0].set_title(f'Dax 30 Last Close', fontsize=20)
axs[1,1].plot(index_data_ret["^FCHI"], color = "green")
axs[1,1].set_title(f'Cac 40 Last Close', fontsize=20)

plt.show()
st.pyplot(fig)

fig, axs = plt.subplots(2,2, figsize=(30, 15))
#Asia and world
axs[0,0].plot(index_data_ret["^NSEI"], color = "orange")
axs[0,0].set_title(f'Nifty 50 Last Close', fontsize=20)
axs[0,1].plot(index_data_ret["^HSI"], color = "orange")
axs[0,1].set_title(f'Hang Seng Last Close', fontsize=20)
axs[1,0].plot(index_data_ret["^N225"], color = "orange")
axs[1,0].set_title(f'Nikkei 225 Last Close', fontsize=20)
axs[1,1].plot(index_data_ret["SWDA.MI"], color = "violet")
axs[1,1].set_title(f'MSCI World Last Close', fontsize=20)


fig.suptitle('Stock Market Indexes - Prices', fontsize=36, y=0.95)
plt.show()
st.pyplot(fig)


st.header("Part 2: Top 10 Best and Worst Performers of the Main Stock Market Indexes")
st.subheader("S&P 500")
#s&p 500 best and worst
sp500url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
data_table = pd.read_html(sp500url)

in_days = 5
in_end_date = date.today()
in_start_date = in_end_date-timedelta(days=in_days)

tickers = data_table[0]["Symbol"].tolist()
com_names = data_table[0]["Security"].tolist()

for i in range(len(tickers)):
    if tickers[i]=="BRK.B":
        tickers[i] = "BRK-B"
    elif tickers[i]=="BF.B":
        tickers[i] = "BF-B"
#tickers.remove("STLD")

gics_sector = data_table[0]["GICS Sector"].tolist()
gics_sub_ind = data_table[0]["GICS Sub-Industry"].tolist()
xlookup = pd.DataFrame({"TIK":tickers, "Company Name":com_names, "GICS Sector":gics_sector, "GICS Sub Industry":gics_sub_ind})
#xlookup = xlookup.drop(xlookup[xlookup["TIK"]=="STLD"].index)
#tickers.remove("STLD")

snp_prices = yf.download(tickers, in_start_date, in_end_date)["Adj Close"]

#date_time_obj = date.today()-timedelta(days=1)
date_time_obj = snp_prices.index[-1]
formatted_date = date_time_obj.strftime('%Y-%m-%d')

snp_ret = snp_prices.pct_change().dropna()
snp_ret = snp_ret*100
snp_ret.index = snp_ret.index.strftime('%Y-%m-%d')
snp_ret = snp_ret.T

#add security name
snp_ret["TIK"] = snp_ret.index
df1 = xlookup
df2 = snp_ret
df1.set_index("TIK", inplace=True)
df2.set_index("TIK", inplace=True)
result = df1.join(df2, how="outer")

worst = result.sort_values(by = formatted_date).head(10).iloc[:,[0,1,2,len(result.T)-1]]
worst = round(worst, 3)

fig, ax = plt.subplots(figsize=(10, 2))  # Imposta la dimensione della figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=worst.values, colLabels=worst.columns, rowLabels=worst.index, cellLoc='center', loc='center')
table.scale(2, 1.8)  # Aumenta larghezza e altezza delle celle
table.set_fontsize(38)

# Color the header
for i in range(4):
    table[0,i].set_text_props(color="white", weight="bold")
    table[0,i].set_facecolor("#000080")  # Set background color for the header

#color the returns
for i in range(len(worst)):
    table[i+1,3].set_facecolor("#FFCCCC")

plt.show()
st.pyplot(fig)

best = result.sort_values(by = formatted_date, ascending=False).head(10).iloc[:,[0,1,2,len(result.T)-1]]
best = round(best, 3)

fig, ax = plt.subplots(figsize=(10, 2))  # Imposta la dimensione della figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=best.values, colLabels=best.columns, rowLabels=best.index, cellLoc='center', loc='center')
table.scale(2, 1.8)  # Aumenta larghezza e altezza delle celle
table.set_fontsize(38)

# Color the header
for i in range(4):
    table[0,i].set_text_props(color="white", weight="bold")
    table[0,i].set_facecolor("#000080")  # Set background color for the header
    
#color the returns
for i in range(len(best)):
    table[i+1,3].set_facecolor("#CCFFCC")

plt.show()
st.pyplot(fig)


st.subheader("Nasdaq 100")
#nasdaq 100
nasdaq100url = 'https://en.wikipedia.org/wiki/Nasdaq-100'
nasq_data_table = pd.read_html(nasdaq100url)

nasq_tickers = nasq_data_table[4]["Symbol"].tolist()
nasq_com_names = nasq_data_table[4]["Company"].tolist()
nasq_gics_sector = nasq_data_table[4]["GICS Sector"].tolist()
nasq_gics_sub_ind = nasq_data_table[4]["GICS Sub-Industry"].tolist()
nadq_prices = yf.download(nasq_tickers, in_start_date, end_date)["Adj Close"]

nasq_ret = nadq_prices.pct_change().dropna()
nasq_ret = nasq_ret*100
nasq_ret.index = nasq_ret.index.strftime('%Y-%m-%d')
nasq_ret = nasq_ret.T

#add gics and name
nasq_ret["TIK"] = nasq_ret.index
xlookup = pd.DataFrame({"TIK":nasq_tickers, "Company Name":nasq_com_names, "GICS Sector":nasq_gics_sector, "GICS Sub Industry":nasq_gics_sub_ind})
df1 = xlookup
df2 = nasq_ret
df1.set_index("TIK", inplace=True)
df2.set_index("TIK", inplace=True)
result = df1.join(df2, how="outer")

nasq_worst = result.sort_values(by = formatted_date).head(10).iloc[:,[0,1,2,len(result.T)-1]]
nasq_worst = round(nasq_worst, 3)

fig, ax = plt.subplots(figsize=(15, 2))  # Imposta la dimensione della figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=nasq_worst.values, colLabels=nasq_worst.columns, rowLabels=nasq_worst.index, cellLoc='center', loc='center')
table.scale(1.6, 2.5)
table.set_fontsize(38)

# Color the header
for i in range(4):
    table[0,i].set_text_props(color="white", weight="bold")
    table[0,i].set_facecolor("#000080")  # Set background color for the header
    
#color the returns
for i in range(len(best)):
    table[i+1,3].set_facecolor("#FFCCCC")  # Set background color for the header

plt.show()
st.pyplot(fig)

nasq_best = result.sort_values(by = formatted_date, ascending=False).head(10).iloc[:,[0,1,2,len(result.T)-1]]
nasq_best = round(nasq_best, 3)

fig, ax = plt.subplots(figsize=(15, 2))  # Imposta la dimensione della figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=nasq_best.values, colLabels=nasq_best.columns, rowLabels=nasq_best.index, cellLoc='center', loc='center')
table.scale(1.6, 2.5) 
table.set_fontsize(38)

# Color the header
for i in range(4):
    table[0,i].set_text_props(color="white", weight="bold")
    table[0,i].set_facecolor("#000080")  # Set background color for the header
    
#color the returns
for i in range(len(best)):
    table[i+1,3].set_facecolor("#CCFFCC")  # Set background color for the header

plt.show()
st.pyplot(fig)

st.subheader("Eurostoxx 50")
stoxx50url = 'https://en.wikipedia.org/wiki/EURO_STOXX_50'
stoxx50_data_table = pd.read_html(stoxx50url)

stoxx50_tickers = stoxx50_data_table[4]["Ticker"].tolist()
for i in range(len(stoxx50_tickers)):
    if stoxx50_tickers[i]=="FLTR.IR":
        stoxx50_tickers[i] = "FLTR.L"

stoxx50_com_names = stoxx50_data_table[4]["Name"].tolist()
stoxx50_industry = stoxx50_data_table[4]["Industry"].tolist()
stoxx50_reg_office = stoxx50_data_table[4]["Registered office"].tolist()

stoxx50_prices = yf.download(stoxx50_tickers, in_start_date, end_date)["Adj Close"]

stoxx50_ret = stoxx50_prices.pct_change().dropna()
stoxx50_ret = stoxx50_ret*100
stoxx50_ret.index = stoxx50_ret.index.strftime('%Y-%m-%d')
stoxx50_ret = stoxx50_ret.T

#add gics and name
stoxx50_ret["TIK"] = stoxx50_ret.index
xlookup = pd.DataFrame({"TIK":stoxx50_tickers, "Company Name":stoxx50_com_names, "Industry":stoxx50_industry, "Registred Office":stoxx50_reg_office})
df1 = xlookup
df2 = stoxx50_ret
df1.set_index("TIK", inplace=True)
df2.set_index("TIK", inplace=True)
result = df1.join(df2, how="outer")

stoxx50_worst = result.sort_values(by = formatted_date).head(10).iloc[:,[0,1,2,len(result.T)-1]]
stoxx50_worst = round(stoxx50_worst, 3)

fig, ax = plt.subplots(figsize=(10, 2))  # Imposta la dimensione della figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=stoxx50_worst.values, colLabels=stoxx50_worst.columns, rowLabels=stoxx50_worst.index, cellLoc='center', loc='center')
table.scale(1.6, 2.5)
table.set_fontsize(38)

# Color the header
for i in range(4):
    table[0,i].set_text_props(color="white", weight="bold")
    table[0,i].set_facecolor("#000080")  # Set background color for the header
    
#color the returns
for i in range(len(stoxx50_worst)):
    table[i+1,3].set_facecolor("#FFCCCC")  # Set background color for the header

plt.show()
st.pyplot(fig)

stoxx50_best = result.sort_values(by = formatted_date, ascending=False).head(10).iloc[:,[0,1,2,len(result.T)-1]]
stoxx50_best = round(stoxx50_best, 3)

fig, ax = plt.subplots(figsize=(10, 2))  # Imposta la dimensione della figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=stoxx50_best.values, colLabels=stoxx50_best.columns, rowLabels=stoxx50_best.index, cellLoc='center', loc='center')
table.scale(1.6, 2.5)
table.set_fontsize(38)

# Color the header
for i in range(4):
    table[0,i].set_text_props(color="white", weight="bold")
    table[0,i].set_facecolor("#000080")  # Set background color for the header
    
#color the returns
for i in range(len(stoxx50_best)):
    table[i+1,3].set_facecolor("#CCFFCC")  # Set background color for the header

plt.show()
st.pyplot(fig)


#bond
st.header("Part 3: Interest Rates and Bond Yield")
st.subheader("Main Policy Rates")

#policy rates
depo_facility_eu = web.DataReader(['ECBDFR'], 'fred', start_date, end_date)
fed_funds_rate = web.DataReader(['DFF'], 'fred', start_date, end_date)
sonia_uk = web.DataReader(["IUDSOIA"], 'fred', start_date, end_date)

plt.figure(figsize=(10, 5))
plt.plot(depo_facility_eu, color = "blue", label = "Deposit Facility EU")
plt.plot(fed_funds_rate, color = "red", label = "Fed Funds")
plt.plot(sonia_uk, color = "yellow", label = "Sonia UK")
plt.ylabel("Policy Rates")
plt.xlabel("Time Horizon")

plt.title('Main Interest Rate (in %)', fontsize=15, y=1)
plt.legend(loc="upper left")
plt.show()
st.pyplot(plt)

st.subheader("10 Year Bond Yield")
int_rate_10Y_usa = web.DataReader(["IRLTLT01USM156N"], 'fred', start_date, end_date)
italy_10_y_yield = web.DataReader(['IRLTLT01ITM156N'], 'fred', start_date, end_date)
germany_10_y_yield = web.DataReader(['IRLTLT01DEM156N'], 'fred', start_date, end_date)
france_10_y_yield = web.DataReader(['IRLTLT01FRM156N'], 'fred', start_date, end_date)
spain_10_y_yield = web.DataReader(['IRLTLT01ESM156N'], 'fred', start_date, end_date)
uk_10_y_yield = web.DataReader(['IRLTLT01GBM156N'], 'fred', start_date, end_date)
japan_10_m_yield = web.DataReader(["IRLTLT01JPM156N"], 'fred', start_date, end_date)

plt.figure(figsize=(10, 5))
plt.plot(int_rate_10Y_usa, color = "blue", label = "USA")
plt.plot(italy_10_y_yield, color = "green", label = "Italy")
plt.plot(germany_10_y_yield, color = "black", label = "Germany")
plt.plot(france_10_y_yield, color = "lightblue", label = "France")
plt.plot(spain_10_y_yield, color = "orange", label = "Spain")
plt.plot(uk_10_y_yield, color = "red", label = "UK")
plt.plot(japan_10_m_yield, color = "violet", label = "Japan")
plt.ylabel("Bond Yield")
plt.xlabel("Time Horizon")

plt.title('10 Year Bond Yield (in %)', fontsize=15, y=1)
plt.legend(loc="upper left")
plt.grid(axis='y')  # Add horizontal grid lines
plt.show()
st.pyplot(plt)


#commodities and FX
st.header("Part 4: Commodities and FX")
st.subheader("Commodities Returns")
general_commodities = ["GC=F", "CL=F", "TTF=F", "ZC=F", "BTC-EUR", "ETH-EUR"]
general_commodities_data = yf.download(general_commodities, start_date, end_date)
general_commodities_data = general_commodities_data["Close"]
general_commodities_column_names = ["Gold", "Crude Oil", "Natural Gas", "Corn", "BTC ETH", "ETH EUR"]
general_commodities_data = general_commodities_data.dropna()
general_commodities_data_ret = general_commodities_data.pct_change()*100
general_commodities_data_ret = general_commodities_data_ret.applymap(lambda x: '{:.2f}'.format(x))
general_commodities_data_ret.columns = general_commodities_column_names
general_commodities_data_ret = general_commodities_data_ret.dropna().tail(5)
general_commodities_data_ret = general_commodities_data_ret.applymap(lambda x: f"{x}%" if pd.notnull(x) else x)

fig, ax = plt.subplots(figsize=(5, 2))  # Imposta la dimensione della figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=general_commodities_data_ret.values, colLabels=general_commodities_data_ret.columns, rowLabels=general_commodities_data_ret.index, cellLoc='center', loc='center')
table.scale(2.2, 1.8) 

# Color the header
for i in range(len(general_commodities)):
    table[0,i].set_text_props(color="white", weight="bold")
    table[0,i].set_facecolor("#000080")  # Set background color for the header

plt.show()
st.pyplot(fig)

fig, axs = plt.subplots(2,3, figsize=(30, 15))
#first line
axs[0,0].plot(general_commodities_data.iloc[0:,3], color = "blue")
axs[0,0].set_title(f'Gold Last Close: {round(general_commodities_data.iloc[len(general_commodities_data)-1:len(general_commodities_data),3], 2).tolist()}', fontsize=20)
axs[0,1].plot(general_commodities_data.iloc[0:,1], color = "blue")
axs[0,1].set_title(f'Crude Oil Last Close: {round(general_commodities_data.iloc[len(general_commodities_data)-1:len(general_commodities_data),1], 2).tolist()}', fontsize=20)
axs[0,2].plot(general_commodities_data.iloc[0:,4], color = "blue")
axs[0,2].set_title(f'Natural Gas Last Close: {round(general_commodities_data.iloc[len(general_commodities_data)-1:len(general_commodities_data),4], 2).tolist()}', fontsize=20)

#second line
axs[1,0].plot(general_commodities_data.iloc[0:,5], color = "blue")
axs[1,0].set_title(f'Corn Last Close: {round(general_commodities_data.iloc[len(general_commodities_data)-1:len(general_commodities_data),5], 2).tolist()}', fontsize=20)
axs[1,1].plot(general_commodities_data.iloc[0:,0], color = "blue")
axs[1,1].set_title(f'Bitcoin EUR Last Close: {round(general_commodities_data.iloc[len(general_commodities_data)-1:len(general_commodities_data),0], 2).tolist()}', fontsize=20)
axs[1,2].plot(general_commodities_data.iloc[0:,2], color = "blue")
axs[1,2].set_title(f'Ethereum EUR Last Close: {round(general_commodities_data.iloc[len(general_commodities_data)-1:len(general_commodities_data),5], 2).tolist()}', fontsize=20)

fig.suptitle('Main Commodities - Prices', fontsize=36, y=0.95)
plt.show()
st.pyplot(fig)

st.subheader("FX Returns")
currencies = ["EURUSD=X", "EURGBP=X", "EURCHF=X", "EURJPY=X"]
currencies_data = yf.download(currencies, start_date, end_date)
currencies_data = currencies_data["Close"]
currencies_column_names = ["USD / EUR", "GBP / EUR", "CHF / EUR", "USD / JPY"]
currencies_data_ret = currencies_data.pct_change()*100
currencies_data_ret = currencies_data_ret.applymap(lambda x: '{:.2f}'.format(x))
currencies_data_ret.columns = currencies_column_names
currencies_data_ret = currencies_data_ret.tail(5)
currencies_data_ret = currencies_data_ret.applymap(lambda x: f"{x}%" if pd.notnull(x) else x)

fig, ax = plt.subplots(figsize=(5, 2))  # Imposta la dimensione della figura
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=currencies_data_ret.values, colLabels=currencies_data_ret.columns, rowLabels=currencies_data_ret.index, cellLoc='center', loc='center')
table.scale(2.2, 1.8) 

# Color the header
for i in range(len(currencies)):
    table[0,i].set_text_props(color="white", weight="bold")
    table[0,i].set_facecolor("#000080")  # Set background color for the header

plt.show()
st.pyplot(fig)

fig, axs = plt.subplots(3,3, figsize=(30, 15))
#first line
axs[0,0].plot(currencies_data.iloc[0:,1], color = "blue")
axs[0,0].set_title(f'USD / EUR:\n {round(currencies_data.iloc[len(currencies_data)-1:len(currencies_data),5], 4).tolist()}', fontsize=12)
axs[0,1].plot(currencies_data.iloc[0:,2], color = "blue")
axs[0,1].set_title(f'GBP / EUR:\n {round(currencies_data.iloc[len(currencies_data)-1:len(currencies_data),3], 4).tolist()}', fontsize=12)

#second line
axs[1,0].plot(currencies_data.iloc[0:,3], color = "blue")
axs[1,0].set_title(f'CHF / EUR:\n{round(currencies_data.iloc[len(currencies_data)-1:len(currencies_data),2], 4).tolist()}', fontsize=12)
axs[1,1].plot(currencies_data.iloc[0:,4], color = "blue")
axs[1,1].set_title(f'EUR / JPY:\n {round(currencies_data.iloc[len(currencies_data)-1:len(currencies_data),1], 4).tolist()}', fontsize=12)

fig.suptitle('Main FX - Quotes', fontsize=36, y=0.94)
plt.show()
st.pyplot(fig)
