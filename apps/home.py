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
    including those that I learned from my readings and from watching 
    instructional videos. This is an application that directly reads-in 
    data from a [Covid-19 API](https://covid19api.com/ ), where current and up-to-date 
    forecasting, a machine learning method, can be done once the API is updated and
    the application is run. I also used an object-oriented-programming to present 
    results in an organized manner by structuring the program into separate python files 
    and generate a multipage application. The app is limited to South East Asian
    Nations to minimize computational time but can easily be extended to other
    regions since I used an API to query my data. Lastly, it is deployed to
    share.streamlit.io to easily share the app for submission to the professor and 
    use of anyone with the link.
    
    I used a [Jupyter Notebook](https://github.com/jerryendrina/535Project/blob/main/staticVersion.ipynb) 
    to create a static version of the app before I translated it to an interactive one.  
    
    The link to my github repository can be found [here](https://github.com/jerryendrina/535Project).  
    
    """)
    
    expander1 = st.expander("The packages I used are:")
    expander1.markdown("""
                       
        1. requests - to query data from the Covid-19 API  
        2. pandas - to perform data manipulation and analysis  
        3. base64 - to create a link where user can download the data  
        4. multiapp - to run the object-oriented-program  
        5. plotly - to generate plots  
        6. fbprophet - to run machine learning or forecasting  
        7. streamlit - to create an interactive dashboard  
    
    """)  
    
    expander2 = st.expander("Links to articles and videos that helped me in this project:")
    expander2.markdown("""
        
    [Object-Oriented-Programming](https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030)  
    [Machine Learning Forecasting](https://facebook.github.io/prophet/)  
    [Multi-page Streamlit Application](https://www.youtube.com/watch?v=nSw96qUbK9o)  
    [Animate Plots in Streamlit](https://www.youtube.com/watch?v=VZ_tS4F6P2A)  
    [Generate Nice Plots](https://plotly.com/graphing-libraries/)  
    
    """)
    
    # Code
    expander3 = st.expander("Codes to create this app:")
    expander3.markdown("""
    
    [Object-Oriented-Programing Code](https://github.com/jerryendrina/535Project/blob/main/multiapp.py)  
    [Code to Create a Multi-page App](https://github.com/jerryendrina/535Project/blob/main/app.py)  
    [Home Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/home.py)  
    [Data Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/data.py)  
    [Bar Chart Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/barcharts.py)  
    [Trend Line Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/trendlines.py)  
    [Time Series Model Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/model.py)
    
    
    """)
    
   
                          
    
    
    
