from tkinter.tix import ButtonBox
import streamlit as st
from datetime import datetime


input_date = st.date_input("Date of transaction",datetime.now())
st.write("Date of transaction: ",input_date)

input_time = st.time_input("Time of transaction",datetime.now())
st.write("Time of transaction: ",input_time)

input_item = st.text_input("Transaction item",placeholder="Type transaction item")

input_amount = st.number_input("Amount",0.0,placeholder="Type amount")

input_currency = st.selectbox("Currency",("HKD","JPY","TWD","KRW","USD"))

input_submit_button = st.button("Submit")
