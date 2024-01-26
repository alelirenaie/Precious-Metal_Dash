import streamlit as st
import plotly.express as px
import pandas as pd

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data["DateTime"] = pd.to_datetime(data["DateTime"], format="%Y-%m-%d %H:%M:%S")

# Create a default plot using Plotly Express
fig = px.line(
    data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=["Gold"],
    color_discrete_map={"Gold": "gold"}
)

# Streamlit app layout
st.set_page_config(
    page_title="Precious Metal Prices 2018-2021",
    page_icon="💰"
)

# Display header
st.title("Precious Metal Prices")
st.markdown("The cost of precious metals between 2018 and 2021")

# Sidebar for user inputs
metal_filter = st.sidebar.selectbox("Select Metal", data.columns[1:], index=1)
date_range = st.sidebar.date_input("Select Date Range", [data.DateTime.min(), data.DateTime.max()])

# Filter data
filtered_data = data.loc[(data.DateTime >= date_range[0]) & (data.DateTime <= date_range[1])]

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
