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


def my_plot(el_x,el_y):
    plt.scatter(df[el_x],df[el_y])
    return plt.show()
my_plot('Mg','Ca') 

file_list =[]
for i in os.listdir('data/'):
    if i.endswith('.csv'):
        file_list.append(i)

def my_plot(el_x, el_y, file_name, x_lim, check):
    df = pd.read_csv('data/' + file_name)
    plt.scatter(df[el_x]/10000, df[el_y]/10000)

    if check:
        plt.xlabel(el_x + ' (wt%)')
        plt.ylabel(el_y + ' (wt%)')
    else:
        plt.xlabel(el_x + ' (wt-ppm)')
        plt.ylabel(el_y + ' (wt-ppm)')
    plt.xlim(0, x_lim)
    plt.axhline(y = df[el_y].mean()/10000, color='g')
    return plt.show()
