import streamlit as st
import pandas as pd

st.title("Border Processing System Dashboard")

st.write("This app shows basic analysis of children flow data.")

# Load data
data = pd.read_excel("HEATHCARE ANALYST PROJECT.xlsx")

st.subheader("Dataset Preview")
st.write(data.head())

st.subheader("Summary Statistics")
st.write(data.describe())

st.subheader("Apprehended Over Time")
st.line_chart(data["Children apprehended and placed in CBP custody"])
