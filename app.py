#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 05:43:59 2021

@author: jeremiasendrinajr
"""

import streamlit as st
from multiapp import MultiApp
from PIL import Image
from apps import home, data, barcharts, trendlines, model # import your app modules here

app = MultiApp()

image = Image.open('Covid-Banner.png')

st.image(image)

st.markdown("""

###### This application is made as final project of Mr. Jeremias Endrina for the course ISE 535.

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Bar Charts", barcharts.app)
app.add_app("Trend Lines", trendlines.app)
app.add_app("Model", model.app)


# The main app
app.run()