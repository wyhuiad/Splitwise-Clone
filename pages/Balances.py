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

st.header("Balances")
for user in user_list:
    st.subheader(user)
    user_df = transactions_df.loc[transactions_df['Paid by'] == user]

    total_amount_HKD = 0
    user_portion = 0
    len_user_df = user_df.shape[0]

    for i in range(len_user_df):
        user_df['For'].iloc[i] = user_df['For'].iloc[i].replace('[','')
        user_df['For'].iloc[i] = user_df['For'].iloc[i].replace(']','')
        user_df['For'].iloc[i] = user_df['For'].iloc[i].replace("'",'')
        user_df['For'].iloc[i] = user_df['For'].iloc[i].split(', ')
        for j in range(len(user_df['For'].iloc[i])):
            user_df['For'].iloc[i][j] = str(user_df['For'].iloc[i][j])
               
        user_df['to HKD'].iloc[i] = user_df['to HKD'].iloc[i].replace('[','')
        user_df['to HKD'].iloc[i] = user_df['to HKD'].iloc[i].replace(']','')
        user_df['to HKD'].iloc[i] = user_df['to HKD'].iloc[i].replace(')','')
        user_df['to HKD'].iloc[i] = user_df['to HKD'].iloc[i].replace('np.float64(','')
        user_df['to HKD'].iloc[i] = user_df['to HKD'].iloc[i].split(', ')
        for j in range(len(user_df['to HKD'].iloc[i])):
            user_df['to HKD'].iloc[i][j] = float(user_df['to HKD'].iloc[i][j])
        
        total_amount_HKD += sum(user_df['to HKD'].iloc[i])
        if user in user_df['For'].iloc[i]:
            person_index = user_df['For'].iloc[i].index(user)
            user_portion += user_df['to HKD'].iloc[i][person_index]
   

    owed_amount = total_amount_HKD
    owed_amount -= user_portion

    st.write('Is owed ',owed_amount, 'HKD in total.')

    st.write('Paid ',total_amount_HKD, 'HKD in total.')
    for currency in currencies:
        temp_df = user_df.loc[user_df['Currency'] == currency]
    
        total_amount = 0
        for amount in temp_df['Amount']:
            total_amount += amount
        
        if total_amount != 0:
            st.write(currency,': ',total_amount)
            st.dataframe(temp_df)
    st.divider()
    

