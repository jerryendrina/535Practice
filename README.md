# [Covid-19 Forecasting Application](https://share.streamlit.io/jerryendrina/535project/main/app.py)
(Click the link/title above to access the application from share.streamlit.io.)

This application aims to package what I learned from my Python class 
including those from my readings and from watching instructional videos. 
This is an application that directly reads-in 
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

The Python packages I used are:  

        1. requests - to query data from the Covid-19 API  
        2. pandas - to perform data manipulation and analysis  
        3. base64 - to create a link where user can download the data  
        4. multiapp - to run the object-oriented-program  
        5. plotly - to generate plots  
        6. fbprophet - to run machine learning or forecasting  
        7. streamlit - to create an interactive dashboard. 


Links to the Python files or codes:   

1. [Object-Oriented-Programing Code](https://github.com/jerryendrina/535Project/blob/main/multiapp.py)  
2. [Code to Create a Multi-page App](https://github.com/jerryendrina/535Project/blob/main/app.py)  
3. [Home Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/home.py)  
4. [Data Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/data.py)  
5. [Bar Chart Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/barcharts.py)  
6. [Trend Line Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/trendlines.py)  
7. [Time Series Model Page Code](https://github.com/jerryendrina/535Project/blob/main/apps/model.py)

Links to the articles and videos that helped me in this project are:

1. [Object-Oriented-Programming](https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030)  
2. [Machine Learning Forecasting](https://facebook.github.io/prophet/)  
3. [Multi-page Streamlit Application](https://www.youtube.com/watch?v=nSw96qUbK9o)  
4. [Animate Plots in Streamlit](https://www.youtube.com/watch?v=VZ_tS4F6P2A)  
5. [Generate Nice Plots](https://plotly.com/graphing-libraries/)  
    




