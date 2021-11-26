#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 06:47:44 2021

@author: jeremiasendrinajr
"""

import streamlit as st               #to create interactive dashboard
import requests                      #to query with covid-1 API
import pandas as pd                  #to work with dataframes
import plotly.express as px          #to produce pretty plots



def app():
    
    st.title("Animated Bar Chart")

    st.markdown("""
    
    This is the animated bar chart page. The sidebar provides variable and 
    country options that we want to plot. It also has a button where we 
    can play and see how the selected variable changes among countries since 
    the start of the pandemic until the current date.
    
    """)
    

     #################### Function to Generate Data #########################
     
    #function that generates all data of a given country
    @st.cache
    #data for each country
    def countryData(country):
        url1 = "https://api.covid19api.com/dayone/country/"                   
        country = country
        url = url1+country                                                    
        payload={}
        headers = {'X-Access-Token': 'a3c98472-2928-4752-9d71-083ce072213c'}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        df = pd.DataFrame(data)
        return df


    ####################### Generate All Data ###############################
    
    #list of SouthEast Asian Countries and variables to loop through
    seCountries = ["brunei","myanmar","cambodia","timor-leste","indonesia",   
                   "malaysia", "philippines","singapore","thailand","vietnam"]
    varsOptions = ["Confirmed", "Deaths", "Recovered", "Active"]
    
    
    #text to show while loading data
    data_load_state = st.text('Loading data and creating chart...')


    # Generating all data from the API
    bigData = []
    for country in seCountries:
        df = countryData(country)
        bigData.append(df)
    bigData = pd.concat(bigData)
    
    
    ######################## cleaning and filtering ##########################
    
    bigData = bigData[['Country', 'CountryCode','Confirmed','Deaths',
                       'Recovered','Active','Date']]
    bigData['Date'] = pd.to_datetime(bigData.Date, format='%Y-%m-%d %H:%M:%S')
    bigData['Date'] = bigData['Date'].dt.strftime('%Y-%m-%d')
    bigData['Date']= pd.to_datetime(bigData["Date"])
    bigData = bigData.reset_index(drop=True)
    bigData['Date'] = pd.to_datetime(bigData['Date']).dt.strftime('%Y-%m-%d')
    
    
    ##################### Create Animated Bar Chart ##########################
    
    #generate options for sidebar widgets
    bigData['Date'] = pd.to_datetime(bigData['Date']).dt.strftime('%Y-%m-%d')
    countriesCap = bigData['Country'].unique().tolist()
    
    #create sidebar widgets
    varSelected = st.sidebar.selectbox('Which variable would you like to plot?', 
                                       varsOptions, 0) 
    country = st.sidebar.multiselect('Which country/countries would you like to see?', 
                                     countriesCap, ['Philippines', 'Thailand', 
                                                    'Indonesia'])
    
    #filter data based on specified values in the widgets
    showData = bigData[bigData['Country'].isin(country)]
    
    #generate animated bar chart
    fig = px.bar(showData, x="Country", y=varSelected, color="Country", 
                     animation_frame="Date", animation_group="Country")

    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 20

    #notify data is loaded
    data_load_state.text("Data loaded and chart created!")
    
    #display animated bar chart
    st.subheader(f"Animated Bar Chart of {varSelected} Cases for {str(country)[1:-1]}")   
    fig.update_layout(width=800)
    st.write(fig)
    
    
    
    
   
    
    
    


   