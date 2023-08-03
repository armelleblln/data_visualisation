import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure
#from ipywidgets import interact
import os


st.write('Hello world')

file_name_list = []
for i in os.listdir(): 
  if i.endswith('csv'):
    file_name_list.append(i)

st.write(file_name_list)
  

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)


el_list = df.columns.tolist()[27:80]
st.selectbox('select element',[el_list])


st.multiselect('select location', file_name_list,file_name_list[0]) #add the first location as a default option 
