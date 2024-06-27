import streamlit as st
import pandas as pd
from datetime import datetime

# CONSTANTS
currencies_dict = {"HKD":999,"JPY":3,"TWD":7,"KRW":10,"USD":1,"CNY":9}

input_date = st.date_input("Date of transaction",datetime.now())
st.write("Date of transaction: ",input_date)

input_time = st.time_input("Time of transaction",datetime.now())
st.write("Time of transaction: ",input_time)

input_item = st.text_input("Transaction item",placeholder="Type transaction item")

input_amount = st.number_input("Amount",0.0,placeholder="Type amount")

input_currency = st.selectbox("Currency",tuple(currencies_dict.keys()))

# get active users
if "active_users" in st.session_state:
    active_users = st.session_state["active_users"]
else:
    active_users = []

paid_by = st.radio("Paid by",active_users)

split_with = st.multiselect("Split with",active_users)
# input_amount to HKD

if 'exchange_rate' in st.session_state:
    rate_data = st.session_state['exchange_rate']
else:
    exchange_df = pd.read_csv("exchange_rate.csv")
    exchange_df.drop(columns=exchange_df.columns[0],axis=1,inplace=True)
    exchange_df.drop(columns=exchange_df.columns[23:],axis=1,inplace=True)
    rate_data = exchange_df.iloc[0]

if input_currency == "HKD":
    rate = 1
else:
    rate = rate_data[currencies_dict[input_currency]] 

amount_HKD = input_amount * rate
st.write("Rate of currency: ", rate)
st.write("Transaction amount in HKD: ", amount_HKD)

input_submit_button = st.button("Submit")
