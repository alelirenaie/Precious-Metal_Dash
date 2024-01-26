import streamlit as st
import plotly.express as px
import pandas as pd

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data["DateTime"] = pd.to_datetime(data["DateTime"], format="%Y-%m-%d %H:%M:%S")

# Set custom colors
background_color = "#1E1E1E"  # Dark background
text_color = "#FFFFFF"  # White text

# Streamlit app layout customization
st.set_page_config(
    page_title="Precious Metal Prices 2018-2021",
    page_icon="💰",
    layout="wide",  # Adjust the layout as needed
)

# Customize Streamlit title and description
st.title("💰 Precious Metal Prices 2018-2021")
st.markdown("The cost of precious metals between 2018 and 2021")

# Metal Filter
selected_metal = st.selectbox("Select Metal", data.columns[1:], index=0)

# Date Range Filter
start_date = st.date_input("Start Date", min_value=data["DateTime"].min().date(), max_value=data["DateTime"].max().date(), value=data["DateTime"].min().date())
end_date = st.date_input("End Date", min_value=data["DateTime"].min().date(), max_value=data["DateTime"].max().date(), value=data["DateTime"].max().date())

filtered_data = data.loc[(data.DateTime >= str(start_date)) & (data.DateTime <= str(end_date))]

# Plotly Chart with custom colors
fig = px.line(
    filtered_data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=[selected_metal],
    color_discrete_map={
        "Platinum": "#E5E4E2",
        "Gold": "gold",
        "Silver": "silver",
        "Palladium": "#CED0DD",
        "Rhodium": "#E2E7E1",
        "Iridium": "#3D3C3A",
        "Ruthenium": "#C9CBC8"
    }
)

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title="Price (USD/oz)",
    font=dict(
        family="Verdana, sans-serif",
        size=18,
        color=text_color
    ),
    plot_bgcolor=background_color,  # Set background color
    paper_bgcolor=background_color,  # Set background color
)

# Display Plotly Chart
st.plotly_chart(fig, use_container_width=True)
