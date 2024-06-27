# Show all transactions using Data editor, lock all except amount, paid by, for columns

import streamlit as st
import pandas as pd

transactions_df = st.session_state['transactions_df']

st.data_editor(st.session_state['transactions_df'])

if st.button("Refresh"):
    st.rerun