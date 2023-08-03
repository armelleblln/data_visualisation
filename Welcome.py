import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
from bokeh.plotting import figure
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

x = [1:20]
y = [6, 7, 2, 4, 5, 10, 23, 55, 5, 3, 16, 72, 3, 4, 5, 11, 21, 55, 15, 2]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

#p.line(x, y, legend_label='Trend', line_width=2)
p.circle(x, y, legend_label='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)



