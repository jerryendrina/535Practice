#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 06:47:44 2021

@author: jeremiasendrinajr
"""

import streamlit as st
import requests                      #to query with covid-1 API
import pandas as pd                  #to work with dataframes
import plotly.express as px          #to produce pretty plots



def app():
    
    st.title("Bar Charts")

    st.write('This is the ***visualizations*** page.')
    

    ############# Function to Generate Data ################

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
    varsOptions = ["Confirmed", "Deaths", "Recovered", "Active"]


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
    bigData['Date'] = pd.to_datetime(bigData['Date']).dt.strftime('%Y-%m-%d')
    
    
    
    
    
    
    
    ############ Create Animated Bar Chart #####################
    bigData['Date'] = pd.to_datetime(bigData['Date']).dt.strftime('%Y-%m-%d')
    countriesCap = bigData['Country'].unique().tolist()

    varSelected = st.sidebar.selectbox('Which variable would you like to plot?', varsOptions, 0) 
    country = st.sidebar.multiselect('Which country/countries would you like to see?', 
                                     countriesCap, ['Philippines', 'Thailand', 'Indonesia'])
    showData = bigData[bigData['Country'].isin(country)]
    

    fig = px.bar(showData, x="Country", y=varSelected, color="Country", 
                     animation_frame="Date", animation_group="Country")

    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 20

    st.subheader(f"Animated Bar Chart of {varSelected} Cases for {str(country)[1:-1]}")   
    fig.update_layout(width=800)
    st.write(fig)
    
    
    
    
   
    
    
    


   