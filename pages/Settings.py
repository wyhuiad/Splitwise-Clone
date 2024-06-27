import streamlit as st
import pandas as pd

st.header("Upload Exchange Rate")

exchange_rate_file = st.file_uploader("Exchange Rate File")

if exchange_rate_file is not None:
     exchange_df = pd.read_csv(exchange_rate_file)
     
else:
     exchange_df = pd.read_csv("exchange_rate.csv")     
     

exchange_df.drop(columns=exchange_df.columns[0],axis=1,inplace=True)
exchange_df.drop(columns=exchange_df.columns[23:],axis=1,inplace=True)
rate_data = exchange_df.iloc[0]
st.session_state['exchange_rate'] = rate_data

st.table(rate_data)

st.divider()

st.header("Set Users")


if "active_users" in st.session_state:
     user_list = st.session_state["active_users"]
else:
     user_list = []


input_user = st.text_input("Input a user",placeholder="Name")
if st.button("Add"):
     user_list.append(input_user)
     st.session_state["active_users"] = user_list

st.write("Active Users: ",user_list)

if st.button("CLEAR USERS",type="primary"):
     user_list = []
     st.session_state["active_users"] = user_list
