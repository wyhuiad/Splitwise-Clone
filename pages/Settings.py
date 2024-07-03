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
     users_txt = open("users.txt","a+")
     users_txt.seek(0)
     user_list = users_txt.read().splitlines()
     users_txt.close()
     for user in user_list:
          user = user.replace('\n','')
     st.session_state["active_users"] = user_list


input_user = st.text_input("Input a user",placeholder="Name")
if st.button("Add"):
     user_list.append(input_user)
     st.session_state["active_users"] = user_list
     users_txt = open('users.txt','w')
     users_txt.writelines([f"{user}\n" for user in user_list])
     users_txt.close()

st.write("Active Users: ",user_list)

if st.button("CLEAR USERS",type="primary"):
     user_list = []
     st.session_state["active_users"] = user_list
     open('users.txt','w').close()
