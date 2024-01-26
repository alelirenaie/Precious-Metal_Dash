import streamlit as st
import plotly.express as px
import pandas as pd

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data["DateTime"] = pd.to_datetime(data["DateTime"], format="%Y-%m-%d %H:%M:%S")

# Streamlit app layout
st.set_page_config(
    page_title="Precious Metal Prices 2018-2021"
   # page_icon="💰"
)

# Display header
st.title("Precious Metal Prices")
st.markdown("The cost of precious metals between 2018 and 2021")

# Sidebar for user inputs
metal_filter = st.sidebar.selectbox("Select Metal", data.columns[1:], index=1)

# Create a range slider for date selection
start_date, end_date = st.sidebar.date_slider(
    "Select Date Range",
    min_value=data["DateTime"].min(),
    max_value=data["DateTime"].max(),
    value=(data["DateTime"].min(), data["DateTime"].max())
)

# Filter data
filtered_data = data.loc[(data["DateTime"] >= start_date) & (data["DateTime"] <= end_date)]

# Display chart
st.plotly_chart(px.line(
    filtered_data,
    title=f"Precious Metal Prices 2018-2021 - {metal_filter}",
    x="DateTime",
    y=[metal_filter],
    color_discrete_map={
        "Platinum": "#B4B8C4",
        "Gold": "#FFD700",
        "Silver": "#C0C0C0",
        "Palladium": "#FF914D",
        "Rhodium": "#8E9EAB",
        "Iridium": "#9BF6FF",
        "Ruthenium": "#D3A297"
    }
).update_layout(
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title=f"Price ({metal_filter} - USD/oz)",
    font=dict(family="Arial", size=18, color="white")
))

# Display footer
st.markdown("Designed with ❤️ by AleliRenaie")
