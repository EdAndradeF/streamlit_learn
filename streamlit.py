import streamlit as st
import pandas as pd

st.write('Meu primeiro app')
st.write('hahahahahha')
file = st.file_uploader('upload .csv')

if file:
    df = pd.read_csv(file)
    if st.checkbox('filter colunas'):
        select_columns = df.columns
        select_columns = st.multiselect('escolha', select_columns)
        n_rows = st.number_input('numero de linhas', min_value=1, step=1)
        st.write(df.loc[:, select_columns].head(n_rows))

else:
    st.write('coloque o csv do pokemon')

