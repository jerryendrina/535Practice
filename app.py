#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 05:43:59 2021

@author: jeremiasendrinajr
"""


import streamlit as st
from multiapp import MultiApp
from PIL import Image
from apps import home, data, barcharts, trendlines, model 

#write function as an object
app = MultiApp()

#insert image in the front page
image = Image.open('Covid-Banner.png')
st.image(image)

#insert a text in the frontpage
st.markdown("""

###### This application is made as a final project of Mr. Jeremias Endrina for the course ISE 535.

""")

# Add all applications
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Animated Bar Chart", barcharts.app)
app.add_app("Trend Line", trendlines.app)
app.add_app("Time Series Model", model.app)


# The main app
app.run()