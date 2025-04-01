import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load Date Dimension CSV
df_dim_date = pd.read_csv('../data/dim_date.csv', dtype={'date_key': str})

# Load Real Estate Data
df_real_estate = pd.read_csv('../data/annonces.csv')
df_real_estate['Date'] = pd.to_datetime(df_real_estate['Date'], format='%d/%m/%Y')
df_real_estate['date_key'] = df_real_estate['Date'].dt.strftime('%Y%m%d')

# Clean and convert 'Prix' column to numeric
df_real_estate['Prix'] = pd.to_numeric(df_real_estate['Prix'].str.replace(r'\s+', '', regex=True), errors='coerce')
df_real_estate = df_real_estate.dropna(subset=['Prix'])  # Drop rows with invalid 'Prix'

# Join with Date Dimension
df_joined = df_real_estate.merge(df_dim_date, on='date_key', how='left')

# Create visualizations
fig_price_trend = px.line(df_joined, x='Date', y='Prix', title='Price Trend Over Time', markers=True)
fig_price_distribution = px.histogram(df_joined, x='Prix', title='Price Distribution', nbins=20)
fig_property_type = px.bar(df_joined.groupby('Type de bien')['Prix'].mean().reset_index(), x='Type de bien', y='Prix', title='Average Price by Property Type')
fig_location_price = px.box(df_joined, x='Localisation', y='Prix', title='Price Distribution by Location')

# Dash App
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Real Estate Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(id='price-trend', figure=fig_price_trend),
    dcc.Graph(id='price-distribution', figure=fig_price_distribution),
    dcc.Graph(id='property-type-price', figure=fig_property_type),
    dcc.Graph(id='location-price', figure=fig_location_price)
])

if __name__ == '__main__':
    app.run(debug=True)