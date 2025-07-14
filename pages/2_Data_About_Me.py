import streamlit as st
import pandas as pd
import json
infile = open("data.json")
bdata = json.load(infile)[0]

# Header

def header():
    st.header("My Hobbies")
    st.write("I want to share my hobbies and see if you have similar hobbies as me!")
    st.write("---")
header()

if st.checkbox("Click here!"):
    st.header("SPORTS!!!")
    st.subheader("My favorite:")
    st.write("My favorite sport is baseball.")
    st.write("---")
    if st.checkbox("Option 1"):
        st.subheader("Rank your favorites")
        my_value_base = st.slider("Baseball", 0, 10) #NEW
        my_value_bask = st.slider("Basketball", 0, 10)
        my_value_foot = st.slider("Football", 0, 10)
        my_value_hock = st.slider("Hockey", 0, 10)
        my_value_soc = st.slider("Soccer", 0, 10)
        chart_data = pd.DataFrame([my_value_base, my_value_bask, my_value_foot, my_value_soc, my_value_hock], ["Baseball", "Basketball", "Football", "Soccer", "Hockey"])
        st.bar_chart(chart_data) #NEW
        st.write("---")
    if st.checkbox("Option 2"):
        st.subheader("Favorite Team")
        st.write("My favorite team is the Atlanta Braves")
        st.write("Here are their stats over the last 10 years:")
        st.line_chart(data = bdata, x = "Year", y = "Wins")
    st.write("---")
if st.checkbox("Or here!"):
    st.header("Music!")
    st.subheader("My favorite genre:")
    st.write("My favorite music genre is rock!")
    st.subheader("What's yours?")
    country = st.slider("Country", 0, 10)
    dance = st.slider("Dance", 0, 10)
    hip_hop = st.slider("Hip Hop", 0, 10)
    jazz = st.slider("Jazz", 0, 10)
    pop = st.slider("Pop", 0, 10)
    rock = st.slider("Rock", 0, 10)
    chart_data = pd.DataFrame([country, dance, hip_hop, jazz, pop, rock], ["Country", "Dance", "Hip Hop", "Jazz", "Pop", "Rock"])
    st.line_chart(chart_data)
