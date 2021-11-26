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

import streamlit as st               #to create interactive dashboard
import requests                      #to query with covid-1 API
import pandas as pd                  #to work with dataframes
import plotly.express as px          #to produce pretty plots



def app():
    st.title('Trend Line')

    st.markdown("""
    
    This is the trend line page. Plotting our time series data help us see 
    trends visually. This can give us an initial idea of how our future predictions 
    might look like. The sidebar provides variable and country options that we 
    want to plot. Plotly is a great visualization package where we can zoom in
    and see closely the values of the plot.
    
    """)
    
    @st.cache
    ### function to generate data ####
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

    ######################## generate data  ###################################
    
    countriesCap = ["Brunei Darussalam", "Myanmar", "Cambodia", "Timor-Leaste",
                    "Indonesia", "Malaysia", "Philippines", "Singapore", 
                    "Thailand", "Viet Nam"]
    countryLine = st.sidebar.selectbox('Which country would you like to plot?', 
                                       countriesCap, 6) 
    
    #text to show while loading data
    data_load_state = st.text('Loading data and creating trend line...')
    
    #query data from API
    data = countryData(countryLine)
    data = data.iloc[:-1 , :]
    
    #notify data is loaded
    data_load_state.text("Data loaded and trend line created!")
    
    #Create daily cases
    data['DailyCases'] = data['Confirmed'].diff()
    data = data.dropna()
    data['DailyCases'] = data['DailyCases'].astype(int)

    #Create daily deaths
    data['DailyDeaths'] = data['Deaths'].diff()
    data = data.dropna()
    data['DailyDeaths'] = data['DailyDeaths'].astype(int)
    
    
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    
    
    varsOptions = ['Confirmed','Deaths','Recovered','Active','DailyCases', 
                   'DailyDeaths']
    varSelected = st.sidebar.selectbox('Which variable would you like to plot?', 
                                       varsOptions, 4) 
    
    
    ######################## Create Trend Lines ##############################
    
    st.subheader(f"Trend Line of the Variable '{varSelected}' for {countryLine}")
    
    dataScat = data[['Country', varSelected, 'Date']]
    fig2 = px.line(dataScat, x="Date", y=varSelected)
    st.write(fig2)
    
    
   
    
    
    


   