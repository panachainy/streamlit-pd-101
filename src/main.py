from pandasai import SmartDataframe
from langchain_community.llms import Ollama
import pandas as pd
import streamlit as st

# st.page_link("main.py", label="Home", icon="🏠")
# st.page_link("pages/ex.py", label="ex", icon="1️⃣")

st.write('This is example for money lover application exported data')


@st.cache_resource
def pd_transaction_csv():
    return pd.read_csv('datas/2024-11-05.csv',
                       encoding='utf-16',
                       sep='\t',
                       header=0,
                       names=['Id', 'Date', 'Category', 'Amount',
                              'Currency', 'Note', 'Wallet']
                       )


data = pd_transaction_csv()
dt = pd.DataFrame(data.head())
st.dataframe(dt)

# ===


llm = Ollama(model="mistral")
df = SmartDataframe(data, config={"llm": llm},)

with st.form('data_prompt_form'):
    text = st.text_area(
        label='Prompt data here:', placeholder='Which Category expensive in 2024?'
    )
    submitted = st.form_submit_button('Submit')
    if submitted:
        with st.status(label="Running...", expanded=True, state="running") as status:
            try:
                st.write(df.chat(text))
                status.update('Completed', expanded=False, state="complete")
            except Exception as e:
                status.update(label=f"An error occurred: {e}", state="error")


# st.chat_input(placeholder="Your message",  key=None, max_chars=None,
#               disabled=False, on_submit=None, args=None, kwargs=None)

# st.chat_message('name',   avatar=None)


# if st.button('Chat data', key='show_data'):
#     st.status('Running', expanded=False, state="running")
#     c = df.chat('Which are top 5 Category amount is expensive')

#     st.write(c)
#     st.status('Done', expanded=False, state="complete")
