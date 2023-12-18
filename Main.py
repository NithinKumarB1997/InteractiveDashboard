import streamlit as st
import datetime
import yfinance as yf
import pandas as pd
import sqlite3
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import pyodbc
from st_aggrid import AgGrid
from streamlit_extras.metric_cards import style_metric_cards # beautify metric card with css
from streamlit_extras.grid import grid 


st.set_page_config(page_title="Portfolio Dashboard", page_icon=":bar_chart:", layout="wide")

data = pd.read_csv("FUNDS.csv")

with st.container():
    st.markdown("<h1 style='text-align: center;'>Portfolio Dashboard</h1>", unsafe_allow_html=True)

with st.container():
    
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader('Real')
            m1,m2 = st.columns(2)
            with m1:
                st.metric(label="Profitability", value= '$123.12')
                style_metric_cards(border_left_color="#DBF227")
            with m2:
                st.metric(label="Volatility", value= '$176.45')
                style_metric_cards(border_left_color="#DBF227")

    with col2:
        with st.container(border=True):
            st.subheader('Model')
            m1,m2 = st.columns(2)
            with m1:
                st.metric(label="Profitability", value= '$456.31')
                style_metric_cards(border_left_color="#DBF227")
            with m2:
                st.metric(label="Volatility", value= '$487.24')
                style_metric_cards(border_left_color="#DBF227")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader('Funds')

            my_grid = grid(2, vertical_align="bottom")
            my_grid.selectbox( "Fund-1",data["FUNDS"].unique())
            my_grid.text_input("Enter Fund1 Value")

            my_grid.selectbox( "Fund-2",data["FUNDS"].unique())
            my_grid.text_input("Enter Fund2 Value")

            my_grid.selectbox( "Fund-3",data["FUNDS"].unique())
            my_grid.text_input("Enter Fund3 Value")

            my_grid.selectbox( "Fund-4",data["FUNDS"].unique())
            my_grid.text_input("Enter Fund4 Value")

            my_grid.selectbox( "Fund-5",data["FUNDS"].unique())
            my_grid.text_input("Enter Fund5 Value")

        
    with col2:
        with st.container(border=True):
            st.subheader('Expected Volatility')
            st.metric(label="Local Fixed Income", value= '')
            style_metric_cards(border_left_color="#DBF227")

            st.metric(label="Local Variable Income", value= '')
            style_metric_cards(border_left_color="#DBF227")

