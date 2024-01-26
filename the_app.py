import streamlit as st
import plotly.express as px
import pandas as pd

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data["DateTime"] = pd.to_datetime(data["DateTime"])

# Create a plotly plot for use by st.plotly_chart().
fig = px.line(
    data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=["Gold"],
    color_discrete_map={"Gold": "gold"}
)

# Streamlit app layout
st.set_page_config(page_title="Precious Metal Prices 2018-2021", page_icon=":moneybag:")

# Sidebar
st.sidebar.title("Options")
metal_filter = st.sidebar.selectbox("Metal", data.columns[1:], index=1)
date_range = st.sidebar.date_input("Date Range", [data.DateTime.min().date(), data.DateTime.max().date()])

# Filter data
filtered_data = data.loc[(data.DateTime >= date_range[0]) & (data.DateTime <= date_range[1])]

# Display header
st.title("Precious Metal Prices")
st.markdown("The cost of precious metals between 2018 and 2021")

# Display chart
st.plotly_chart(fig.update_traces(y=[metal_filter], color_discrete_map={"Gold": "gold"}))

# Display footer
st.markdown("Designed with ❤️ by AleliRenaie")
