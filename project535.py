#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:36:15 2021

@author: jeremiasendrinajr
"""
import numpy as np                   #to work with arrays    
import pandas as pd                  #to work with dataframes
import requests                      #to query with covid-1 API
import datetime                      #to work with time values
from datetime import datetime        #to work with time values
import streamlit as st
import plotly.express as px          #to produce pretty plots
from PIL import Image
import base64                        #to download csv file

# Page Layout
st.set_page_config(layout="wide") 

# Title
#image = Image.open('logo.jpg')
#st.image(image, width=500)



st.title('Covid-19 Forecasting App')
st.markdown("""
            
This app retrieves data from a **Covid-19 API**!

""")


# About
expander_bar = st.expander("About")
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
* **Data source:** [CoinMarketCap](http://coinmarketcap.com).
* **Credit:** Web scraper adapted from the Medium article *[Web Scraping Crypto Prices With Python](https://towardsdatascience.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)* written by [Bryan Feng](https://medium.com/@bryanf).
""")


# Sidebar Layout
col1 = st.sidebar
col2, col3 = st.columns((1,1))

col1.header('Input Options')

country_selected = col1.selectbox('Select country to forecast:', 
                                     ('Philippines', 'Thailand', 'Malaysia', 'Indonesia'))



############# Functions to Generate Data ################

@st.cache
#data for each country
def countryData(country):
    url1 = "https://api.covid19api.com/dayone/country/"                   #base url to be queried
    country = country
    url = url1+country                                                    #complete url to be queried
    payload={}
    headers = {'X-Access-Token': 'a3c98472-2928-4752-9d71-083ce072213c'}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    df = pd.DataFrame(data)
    return df



############# Generate All Data ###############
#list of SouthEast Asian Countries and variables
seCountries = ["brunei","myanmar","cambodia","timor-leste","indonesia",   #create a list of South East Asian nations
               "malaysia", "philippines","singapore","thailand","vietnam"]
variables = ["Country","CountryCode", "Confirmed", "Deaths", "Recovered", "Active", "Date"]


# Generating all data from the API
bigData = []
for country in seCountries:
    df = countryData(country)
    bigData.append(df)
bigData = pd.concat(bigData)

#cleaning and filtering for visualization and forecasting
bigData = bigData[['Country', 'CountryCode','Confirmed','Deaths','Recovered','Active','Date']]
bigData['Date'] = pd.to_datetime(bigData.Date, format='%Y-%m-%d %H:%M:%S')
bigData['Date'] = bigData['Date'].dt.strftime('%Y-%m-%d')
bigData['Date']= pd.to_datetime(bigData["Date"])
bigData = bigData.reset_index(drop=True)



############ Create Table to Render ###########
#filter columns
countriesCap = bigData['Country'].unique().tolist()
vars_selected = col1.multiselect('Select Variables:', variables, variables)
nations_selected = col1.multiselect('Filter Country:', countriesCap, countriesCap)

df1 = bigData[ (bigData['Country'].isin(nations_selected)) ]
df2 = df1[vars_selected]

col2.subheader("Covid-19 Data of Selected Country")
col2.write('Data Dimension: ' + str(df2.shape[0]) + ' rows and ' + str(df2.shape[1]) + ' columns.')
col2.dataframe(df2)


# Download CSV data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
    return href

col2.markdown(filedownload(df2), unsafe_allow_html=True)





############ Create Plots #####################
bigData['Date'] = pd.to_datetime(bigData['Date']).dt.strftime('%Y-%m-%d')
dateOptions = bigData['Date'].unique().tolist()

#date = st.sidebar.selectbox('Which datea would you like to see?', dateOptions, 100)
country = st.sidebar.multiselect('Which country/countries would you like to see?', 
                                 countriesCap, ['Philippines'])

showData = bigData[bigData['Country'].isin(country)]
#showData = bigData[bigData['Date']==date]

st.write(showData)




fig = px.bar(showData, x="Country", y="Confirmed", color="Country", 
                 animation_frame="Date", animation_group="Country")

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 30
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

fig.update_layout(width=800)
st.write(fig)



