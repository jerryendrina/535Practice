#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 05:50:32 2021

@author: jeremiasendrinajr
"""

import streamlit as st
import requests                      #to query with covid-1 API
import pandas as pd                  #to work with dataframes
from fbprophet import Prophet
import plotly.graph_objs as go       #to produce pretty plots




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
    
    seCountries = ["brunei","myanmar","cambodia","timor-leste","indonesia",   #create a list of South East Asian nations
                   "malaysia", "philippines","singapore","thailand","vietnam"]
    countrySel = st.sidebar.selectbox('Which country would you like to forecast?', seCountries, 0) 
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
    
    #### generate table of numerical summaries #####
    varsOptions = ['Confirmed','Deaths','Recovered','Active','DailyCases', 'DailyDeaths']
    varSelected = st.sidebar.selectbox('Which variable would you like to forecast?', varsOptions, 4) 
    table = data[varSelected].describe().to_frame()
    st.dataframe(table)
    
    
    
    ###### forecasting using prophet package #######
    #prepare data
    df = data[[varSelected, 'Date']]
    df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d %H:%M:%S')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df['Date']= pd.to_datetime(df["Date"])
    df.columns = ['y', 'ds']

    #fit model using Prophet
    m = Prophet(interval_width=0.95, yearly_seasonality=True)
    model = m.fit(df)

    #generate predictions using model fit
    daysFC = st.sidebar.selectbox('How many days would you like to forecast?', [7,14,30,60] , 0) 
    future = m.make_future_dataframe(periods=int(daysFC), freq='D')
    forecast = m.predict(future)

    #print prediction of the next few days
    forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(int(daysFC))
    
    ####### display forecasted values ######
    forecastDF = forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(int(daysFC))
    st.dataframe(forecastDF)
    
    
    
    ###### generate plot  ######
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
        title=f'Actual and Forecasted {varSelected} Cases for {countrySel}',
        hovermode="x")
    
    st.write(fig3)
    
    
    
    
    
    
    
    

    




    
    
    
    

    