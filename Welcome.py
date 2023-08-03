import streamlit as st
import pandas as pd
st.write('Hello world')

df = pd.read_csv('Baical Rift Zone.csv')
st.dataframe(df)
