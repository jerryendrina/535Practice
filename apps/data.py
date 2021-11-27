#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:36:15 2021

@author: jeremiasendrinajr
"""

import streamlit as st               #to create interactive dashboard
import requests                      #to query with covid-19 API
import pandas as pd                  #to work with dataframes
import base64                        #to download csv file

#write a function that shows data page once data is clicked
def app():
    
    st.title('Data')

    st.markdown("""
    
    This is the dataset page of the application. All data are generated using 
    functions that query from the Covid-19 API. A sidebar provides date, variable
    and country options that we want to display. There is also a link/button 
    where we can download the dataset based on our specified options.
    
    """)

    #################### Function to Generate Data #########################
   
    #function that generates all data of a given country
    @st.cache
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
    varsOptions = ["Country","CountryCode", "Confirmed", "Deaths", "Recovered", 
                   "Active", "Date"]
    
    #text to show while loading data
    data_load_state = st.text('Loading data...')
    
    # Generating all data from the API by looping through country and variables
    bigData = []
    for country in seCountries:
        df = countryData(country)
        bigData.append(df)
    bigData = pd.concat(bigData)
    
    #notify data is loaded
    data_load_state.text("Data loaded!")


    ######################## cleaning and filtering ##########################
    
    bigData = bigData[['Country', 'CountryCode','Confirmed','Deaths',
                       'Recovered','Active','Date']]
    bigData['Date'] = pd.to_datetime(bigData.Date, format='%Y-%m-%d %H:%M:%S')
    bigData['Date'] = bigData['Date'].dt.strftime('%Y-%m-%d')
    bigData['Date']= pd.to_datetime(bigData["Date"])
    bigData = bigData.reset_index(drop=True)
    bigData['Date'] = pd.to_datetime(bigData['Date']).dt.strftime('%Y-%m-%d')
    

    ####################### Create Data Set Table ############################
    
    #list options for sidebar widgets
    dateOptions = bigData['Date'].unique().tolist()
    countriesCap = bigData['Country'].unique().tolist()
    
    #create sidebar widgets
    date = st.sidebar.selectbox('Which date would you like to see?',
                                dateOptions, 400)
    country = st.sidebar.multiselect('Which country/countries would you like to see?', 
                                 countriesCap, countriesCap)
    variables = st.sidebar.multiselect('Which variables would like to see?', 
                                        varsOptions, ['Country', 'Confirmed',
                                                      'Deaths','Active','Date'])
    
    #filter data based on options
    showData = bigData[bigData['Country'].isin(country)]
    showData1 = showData[showData['Date']==date]
    showData2 = showData1[variables]

    
    #display data set
    st.subheader("Covid-19 Data of Selected Countries, Variables and Date")
    st.dataframe(showData2)
    st.write('Data Dimension: ' + str(showData2.shape[0]) + ' rows and ' + str(showData2.shape[1]) + ' columns.')
    

    #################### Function to download CSV data ######################

    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File?</a>'
        return href

    st.sidebar.markdown(filedownload(showData2), unsafe_allow_html=True)
    

    
    




    








