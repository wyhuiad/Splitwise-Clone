import streamlit as st
import pandas as pd

exchange_rate_file = st.file_uploader("Upload exchange rate file")

if exchange_rate_file is not None:
     exchange_df = pd.read_csv(exchange_rate_file)
     exchange_df.drop(columns=exchange_df.columns[0],axis=1,inplace=True)
     exchange_df.drop(columns=exchange_df.columns[23:],axis=1,inplace=True)

     rate_data = exchange_df.iloc[0]
     st.table(rate_data)

#st.dataframe()