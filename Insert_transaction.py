import streamlit as st
import pandas as pd
from datetime import datetime

# CONSTANTS
currencies_dict = {"HKD":999,"JPY":3,"TWD":7,"KRW":10,"USD":1,"CNY":9}
transactions_csv_columns = ["Date","Time","Item","Currency","Amount","Paid by","For","Split","to HKD"]

st.header('WiseSplit - Insert transaction')
st.divider()

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
split_column = []
user_amount_sum = 0


if "split_column" not in st.session_state:
    st.session_state["split_column"] = []

for user in split_with:
    amount_for_user = st.number_input(user,value=input_amount/len(split_with))
    split_column.append(amount_for_user)
    user_amount_sum += amount_for_user
    st.session_state["split_column"] = split_column
    st.session_state["user_amount_sum"] = user_amount_sum

st.write(st.session_state["split_column"])

if user_amount_sum != input_amount:
    st.write("The amount for users does not add up to ",input_amount," , please check.")
    st.session_state["Valid"] = False
else:
    st.session_state["Valid"] = True

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
st.write("Rate of currency: ", rate)

split_column_HKD = []

if 'transactions_df' not in st.session_state:
    transactions_df = pd.read_csv("transactions.csv")
    st.session_state['transactions_df'] = transactions_df
else:
    transactions_df = st.session_state['transactions_df']

if st.session_state["Valid"] != False:
    if st.button("Submit"):
        for i in split_column:
            split_column_HKD.append(i*rate)

        new_transaction_df = pd.DataFrame([[input_date,input_time,input_item,input_currency,input_amount,paid_by,split_with,split_column,split_column_HKD]],columns=transactions_csv_columns)
        transactions_df = pd.concat([transactions_df,new_transaction_df],ignore_index=True)
        st.session_state['transactions_df'] = transactions_df

        pd.DataFrame.to_csv(transactions_df,'transactions.csv',index=False)
        st.write('Transaction recorded')
        st.divider()
    else:
        st.divider()

st.write(st.session_state['transactions_df'])
