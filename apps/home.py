#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 05:47:43 2021

@author: jeremiasendrinajr
"""

import streamlit as st         #to create interactive dashboard


#write a function that shows homepage once home is clicked
def app():
    
    st.title('Home')

    st.markdown("""

    This application aims to package what I learned from my Python class 
    including what I taught myself from readings and videos. I developed an 
    application that directly reads-in updated data from a 
    [Covid-19 API](https://covid19api.com/ ), where current and up-to-date 
    forecasting, a machine learning method, can be done once the application 
    is run. I also used an object-oriented-programming to present results in 
    an organized manner by structuring the program into separate python files 
    and generate a multipage application. The app is limited to South East Asian
    Nations to minimize computational time but can easily be extended to other
    regions since I used an API where I query my data.
    
    I used a [Jupyter Notebook](https://github.com/jerryendrina/535Project/blob/main/staticVersion.ipynb) 
    to create a static version of the app before I translated it to an interactive one.  
    
    The link to my github repository can be found [here](https://github.com/jerryendrina/535Project).  
    
    The packages I used are:  
        
        1. requests - to query data from the Covid-19 API  
        2. pandas - to perform data manipulation and analysis  
        3. base64 - to create a link where user can download the data  
        4. multiapp - to run the object-oriented-program  
        5. plotly - to generate plots  
        6. fbprophet - to run machine learning or forecasting  
        7. streamlit - to create an interactive dashboard  
    
    The following are the links to the articles and videos that helped me in this project:  
        
    [Object-Oriented-Programming](https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030)  
    [Machine Learning Forecasting](https://facebook.github.io/prophet/)  
    [Multi-page Streamlit Application](https://www.youtube.com/watch?v=nSw96qUbK9o)  
    [Animate Plots in Streamlit](https://www.youtube.com/watch?v=VZ_tS4F6P2A)  
    [Generate Nice Plots](https://plotly.com/graphing-libraries/)  
    

    """)
    
    # Code
    expander_bar = st.expander("Code to create this page:")
    expander_bar.markdown("""
    * **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
    * **Data source:** [CoinMarketCap](http://coinmarketcap.com).
    * **Credit:** Web scraper adapted from the Medium article *[Web Scraping Crypto Prices With Python](https://towardsdatascience.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)* written by [Bryan Feng](https://medium.com/@bryanf).
    """)
    
