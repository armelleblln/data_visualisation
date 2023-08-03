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


y = [18.40, 20.92, 32.30, 32.03, 27.62, 27.77, 39.33, 21.48, 36.96, 35.78, 36.11, 31.10, 28.73, 29.40]
x = range(1,14)
p = figure(
    title='Temperature in degree Celsius for the DVB Sample',
    y_axis_label='Temperature (\N{DEGREE SIGN}C)',
    x_axis_label='Sample')
p.line(x, y, legend_label='Trend', color = 'orange', line_width=1, line_dash='dashed')
p.circle_dot(x, y, size=14, color='navy', fill_color='orange', alpha = 0.5)
st.bokeh_chart(p, use_container_width=True)



