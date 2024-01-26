# Import necessary libraries
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd


# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data["DateTime"] = pd.to_datetime(data["DateTime"])

# Create a plotly plot for use by dcc.Graph().
fig = px.line(
    data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=["Gold"],
    color_discrete_map={"Gold": "gold"}
)

app = dash.Dash(__name__)
app.title = "Precious Metal Prices 2018-2021"
server = app.server

app.layout = html.Div(
    id="app-container",
    style={"backgroundColor": "#F0F2F5", "color": "#333333", "fontFamily": "Arial"},
    children=[
        html.Div(
            id="header-area",
            children=[
                html.H1(
                    id="header-title",
                    children="Precious Metal Prices",
                    style={"color": "#FFEA00"}  # Neon Yellow
                ),
                html.P(
                    id="header-description",
                    children=("The cost of precious metals", html.Br(), "between 2018 and 2021"),
                    style={"color": "white"}  # White
                ),
            ],
        ),
        html.Div(
            id="menu-area",
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className="menu-title",
                            children="Metal",
                            style={"color": "Black"}  # Black
                        ),
                        dcc.Dropdown(
                            id="metal-filter",
                            className="dropdown",
                            options=[{"label": metal, "value": metal} for metal in data.columns[1:]],
                            clearable=False,
                            value="Gold",
                            style={"backgroundColor": "#FFFFFF"}  # White
                        )
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            className="menu-title",
                            children="Date Range",
                            style={"color": "Black"}  # Black
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.DateTime.min().date(),
                            max_date_allowed=data.DateTime.max().date(),
                            start_date=data.DateTime.min().date(),
                            end_date=data.DateTime.max().date(),
                            style={"backgroundColor": "black", "color": "white"}  # Set the background color to black
                        )
                    ]
                )
            ]
        ),
        html.Div(
            id="graph-container",
            children=dcc.Graph(
                id="price-chart",
                figure=fig,
                config={"displayModeBar": False}
            ),
        ),
        html.Div(
            id="footer-area",
            children=[
                html.P(
                    children="Designed with ❤️ by AleliRenaie",
                    style={"color": "#F0F2F5"}  # Dark Gray
                )
            ],
            style={"backgroundColor": "black", "margin": "0", "padding": "0"}  # Set the background color to black
        ),
    ]
)

@app.callback(
    Output("price-chart", "figure"),
    Input("metal-filter", "value"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date")
)
def update_chart(metal, start_date, end_date):
    filtered_data = data.loc[(data.DateTime >= start_date) & (data.DateTime <= end_date)]
    # Create a plotly plot for use by dcc.Graph().
    fig = px.line(
        filtered_data,
        title="Precious Metal Prices 2018-2021",
        x="DateTime",
        y=[metal],
        color_discrete_map={
            "Platinum": "#B4B8C4",  # Light Gray
            "Gold": "#FFD700",  # Gold
            "Silver": "#C0C0C0",  # Silver
            "Palladium": "#FF914D",  # Orange
            "Rhodium": "#8E9EAB",  # Slate Blue
            "Iridium": "#9BF6FF",  # Light Blue
            "Ruthenium": "#D3A297"  # Dusty Rose
        }
    )

    # Customize the layout of the plot
    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Date",
        yaxis_title="Price (USD/oz)",
        font=dict(
            family="Arial",
            size=18,
            color="white"
        ),
    )

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)



