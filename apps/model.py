#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 05:50:32 2021

@author: jeremiasendrinajr
"""


import streamlit as st               #to create interactive dashboard
import requests                      #to query with covid-1 API
import pandas as pd                  #to work with dataframes
from fbprophet import Prophet        #to run forecasting using machine learning
import plotly.graph_objs as go       #to produce pretty plots
import plotly.express as px          #to create histogram




def app():
    st.title('Model')

    st.markdown("""
     
     Now that we have explored and visualized our data, then we can use these 
     as our historical input to make an informed estimates that are predictive 
     in nature to determine the direction of the future trends or to forecast 
     what could happen in the future. In this project, we used Facebook's 
     rophet Package to forecast timeseries data with non-linear trends such 
     as Covid-19. Prophet is an open source and fast software that provides 
     automated forecasts that can easily be tuned by data scientist or any 
     users of the program. The package was released by Facebook's Core Data 
     Science team. For more information, click 
     [Prophet]('https://facebook.github.io/prophet/'). Similar to the previous
     pages, the sidebar provides variable and country options that we 
     want to plot. In addition, we can specify the number of days that our
     model will predict. Below are the numerical summaries, distribution and
     future forecasts of the variable and country specified. 
     
     """)
    
    @st.cache
    ################### function to generate data ############################
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

    ######################## generate data  ##################################
    
    seCountries = ["brunei","myanmar","cambodia","timor-leste","indonesia",   
                   "malaysia", "philippines","singapore","thailand","vietnam"]
    countrySel = st.sidebar.selectbox('Which country would you like to forecast?', 
                                      seCountries, 6)
    
    #text to show while loading data
    data_load_state = st.text('Loading data and creating summaries and histogram...')
    
    #query data from API
    data = countryData(countrySel)
    data = data.iloc[:-1 , :]
    
    #Create daily cases
    data['DailyCases'] = data['Confirmed'].diff()
    data = data.dropna()
    data['DailyCases'] = data['DailyCases'].astype(int)

    #Create daily deaths
    data['DailyDeaths'] = data['Deaths'].diff()
    data = data.dropna()
    data['DailyDeaths'] = data['DailyDeaths'].astype(int)
    
    #notify data is loaded and graphs created
    data_load_state.text("Data loaded, summaries, histogram and plot created!")
    
    
    ################## numerical summaries and histogram #####################

    #generate table
    varsOptions = ['Confirmed','Deaths','Recovered','Active','DailyCases', 
                   'DailyDeaths']
    varSelected = st.sidebar.selectbox('Which variable would you like to forecast?', 
                                       varsOptions, 4) 
    table = data[varSelected].describe().to_frame()
    
    #display table 
    st.subheader(f"Numerical Summaries of the Variable '{varSelected}' for {countrySel}")
    st.dataframe(table)

    
    #create and display histogram
    st.subheader(f"Histogram of the Variable '{varSelected}' for {countrySel}")
    fig4 = px.histogram(data, x=varSelected)
    st.write(fig4)
    
   
    ################# forecasting using prophet package ######################
    
    #text to show while loading data
    data_load_state = st.text('Forecasting using machine learning is running...')
    
    #prepare data
    df = data[[varSelected, 'Date']]
    df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d %H:%M:%S')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df['Date']= pd.to_datetime(df["Date"])
    df.columns = ['y', 'ds']

    #fit model using Prophet
    m = Prophet(interval_width=0.95, yearly_seasonality=True)
    m.fit(df)

    #generate predictions using model fit
    daysFC = st.sidebar.selectbox('How many days would you like to forecast?', 
                                  [7,14,30,60] , 0) 
    future = m.make_future_dataframe(periods=int(daysFC), freq='D')
    forecast = m.predict(future)

    #print prediction of the next few days
    forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(int(daysFC))
    
    #display forecasted values
    st.subheader(f"{daysFC}-Day Forecast of the Variable '{varSelected}' for {countrySel}")
    forecastDF = forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(int(daysFC))
    st.dataframe(forecastDF)
    
    #notify data is loaded and graphs created
    data_load_state.text(f"{daysFC}-day forecasting done!")
    
    
    ################ generate actual and forecasted plot  ####################
    
    fig3 = go.Figure([
    go.Scatter(
        name='Forecast',
        x=forecast['ds'],
        y=forecast['yhat'],
        mode='lines',
        line=dict(color='rgb(230, 51, 11)'),
    ),
    go.Scatter(
        name='Upper Bound',
        x=forecast['ds'],
        y=forecast['yhat_upper'],
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=1),
        showlegend=False
    ),
    go.Scatter(
        name='Lower Bound',
        x=forecast['ds'],
        y=forecast['yhat_lower'],
        marker=dict(color="#444"),
        line=dict(width=1),
        mode='lines',
        fillcolor='rgba(195, 195, 195, 0.3)',
        fill='tonexty',
        showlegend=False
    ),
    go.Scatter(
        x=df['ds'], 
        y = df['y'], 
        mode='markers', 
        name='Actual'
    )])
    
    fig3.update_layout(
        yaxis_title=f'{varSelected} Cases',
        hovermode="x")
    
    st.subheader(f"Actual and Forecasted Plot of the Variable '{varSelected}' for {countrySel}")
    st.write(fig3)
    
    
    
    
    
    
    
    

    




    
    
    
    

    