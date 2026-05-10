import streamlit as st
import pandas as pd

st.set_page_config(page_title="Healthcare Analyst Project", layout="wide")

st.title("Border Processing System: Load and Flow Analysis (2023–2026)")

st.write("""
This dashboard analyzes the flow of children through CBP and HHS systems,
focusing on system load, inflow, outflow, and transfer efficiency.
""")

# Load data
data = pd.read_excel("HEATHCARE ANALYST PROJECT.xlsx")

# ---------------------------
# DATA PREVIEW
# ---------------------------
st.subheader("Dataset Preview")
st.dataframe(data.head())

# ---------------------------
# KPI SECTION
# ---------------------------
st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    total_apprehended = data["Children apprehended and placed in CBP custody"].sum()
    st.metric("Total Children Apprehended", f"{total_apprehended:,}")

with col2:
    total_hhs = data["Children in HHS Care"].sum()
    st.metric("Total Children in HHS Care", f"{total_hhs:,}")

with col3:
    total_cbp = data["Children in CBP custody"].sum()
    st.metric("Total Children in CBP Custody", f"{total_cbp:,}")

# ---------------------------
# CHARTS
# ---------------------------
st.subheader("Children Apprehended Over Time")
st.line_chart(data["Children apprehended and placed in CBP custody"])

st.subheader("CBP vs HHS System Load")
st.line_chart(
    data[
        [
            "Children in CBP custody",
            "Children in HHS Care"
        ]
    ]
)

st.subheader("Children Discharged from HHS Care")
st.line_chart(data["Children discharged from HHS Care"])

# ---------------------------
# SUMMARY STATISTICS
# ---------------------------
st.subheader("Summary Statistics")
st.write(data.describe())

# ---------------------------
# FOOTER
# ---------------------------
st.success("Dashboard successfully deployed using Streamlit.")
