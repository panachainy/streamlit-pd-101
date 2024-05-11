from pandas import pd
import streamlit as st

st.page_link("main.py", label="Home", icon="🏠")
st.page_link("pages/ex.py", label="ex", icon="1️⃣")

st.write('This is example for money lover application exported data')

# Id,Date,Category,Amount,Currency,Note,Wallet

# datas/2024-11-05.csv

raw_csv = pd.read_csv('datas/2024-11-05.csv')

st.dataframe(raw_csv)

# st.D
