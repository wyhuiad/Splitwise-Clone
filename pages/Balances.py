# Show balances for each active user and settlement value
import streamlit as st
import pandas as pd

currencies = ('HKD','JPY','TWD','KRW','USD','CNY')

if "active_users" in st.session_state:
     user_list = st.session_state["active_users"]
else:
     user_list = []

# Calculate total amount paid by user
transactions_df = st.session_state['transactions_df']


for user in user_list:
    st.write('Data for ',user)
    user_df = transactions_df.loc[transactions_df['Paid by'] == user]
    st.write(user,' has paid')
    for currency in currencies:
        temp_df = user_df.loc[user_df['Currency'] == currency]
    
        total_amount = 0
        for amount in temp_df['Amount']:
            total_amount += amount
        
        if total_amount != 0:
            st.write(currency,': ',total_amount)
            st.dataframe(temp_df)
    st.divider()
    

