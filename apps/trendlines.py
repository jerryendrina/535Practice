#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 11:51:44 2021

@author: jeremiasendrinajr
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 06:47:44 2021

@author: jeremiasendrinajr
"""

import streamlit as st
import requests                      #to query with covid-1 API
import pandas as pd                  #to work with dataframes
import datetime                      #to work with time values
import plotly.express as px          #to produce pretty plots



def app():
    st.title('Model')

    st.write('This is the `Model` page of the multi-page app.')
    
    @st.cache
    ### function to generate data ####
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

    #### generate data  ####
    
    countriesCap = ["Brunei Darussalam", "Myanmar", "Cambodia", "Timor-Leaste",
                    "Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand", "Viet Nam"]
    countryLine = st.sidebar.selectbox('Which country would you like to plot?', countriesCap, 6) 
    
    data = countryData(countryLine)
    data = data.iloc[:-1 , :]
    
    #Create daily cases
    data['DailyCases'] = data['Confirmed'].diff()
    data = data.dropna()
    data['DailyCases'] = data['DailyCases'].astype(int)

    #Create daily deaths
    data['DailyDeaths'] = data['Deaths'].diff()
    data = data.dropna()
    data['DailyDeaths'] = data['DailyDeaths'].astype(int)
    
    
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    
    
    varsOptions = ['Confirmed','Deaths','Recovered','Active','DailyCases', 'DailyDeaths']
    varSelected = st.sidebar.selectbox('Which variable would you like to plot?', varsOptions, 4) 
    
    
    

    
    ############ Create Trend Lines ##############
    
    
    st.subheader(f"Trend Line of {varSelected} Cases for {countryLine}")
    
    dataScat = data[['Country', varSelected, 'Date']]
    fig2 = px.line(dataScat, x="Date", y=varSelected)
    st.write(fig2)
    
    
   
    
    
    


   