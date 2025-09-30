import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Configure the page
st.set_page_config(
    page_title="Climate Data Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🌍 Climate Data Dashboard</h1>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Temperature Trends", "CO2 Levels", "Sea Level Rise"])

# Generate sample climate data
def generate_sample_data():
    dates = pd.date_range(start='2000-01-01', end='2024-12-31', freq='ME')
    
    # Temperature data (simulated global warming trend)
    base_temp = 14.0
    temp_trend = np.linspace(0, 2.0, len(dates))  # 2°C increase over 25 years
    temperature = base_temp + temp_trend + np.random.normal(0, 0.3, len(dates))
    
    # CO2 levels (simulated increase)
    base_co2 = 370
    co2_trend = np.linspace(0, 100, len(dates))  # 100 ppm increase
    co2_levels = base_co2 + co2_trend + np.random.normal(0, 5, len(dates))
    
    # Sea level (simulated rise)
    base_sea_level = 0
    sea_level_trend = np.linspace(0, 100, len(dates))  # 100mm rise
    sea_level = base_sea_level + sea_level_trend + np.random.normal(0, 10, len(dates))
    
    data = pd.DataFrame({
        'date': dates,
        'temperature': temperature,
        'co2_levels': co2_levels,
        'sea_level': sea_level
    })
    
    return data

# Load data
climate_data = generate_sample_data()

if page == "Overview":
    st.header("Climate Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        current_temp = climate_data['temperature'].iloc[-1]
        st.metric("Current Temperature", f"{current_temp:.1f}°C", "+1.2°C since 2000")
    
    with col2:
        current_co2 = climate_data['co2_levels'].iloc[-1]
        st.metric("CO₂ Levels", f"{current_co2:.0f} ppm", "+45 ppm since 2000")
    
    with col3:
        current_sea = climate_data['sea_level'].iloc[-1]
        st.metric("Sea Level Rise", f"{current_sea:.0f} mm", "+85 mm since 2000")
    
    with col4:
        warming_rate = (climate_data['temperature'].iloc[-1] - climate_data['temperature'].iloc[0]) / 25
        st.metric("Warming Rate", f"{warming_rate:.2f}°C/decade")
    
    # Recent trends chart
    st.subheader("Recent Climate Trends (Last 5 Years)")
    recent_data = climate_data[climate_data['date'] >= '2020-01-01']
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=recent_data['date'], y=recent_data['temperature'],
                            mode='lines', name='Temperature', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=recent_data['date'], y=recent_data['co2_levels']/20,
                            mode='lines', name='CO₂ (scaled)', line=dict(color='blue')))
    
    fig.update_layout(
        title="Temperature and CO₂ Trends",
        xaxis_title="Date",
        yaxis_title="Temperature (°C) / CO₂ (ppm/20)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif page == "Temperature Trends":
    st.header("Global Temperature Analysis")
    
    # Temperature trend chart
    fig = px.line(climate_data, x='date', y='temperature',
                  title="Global Temperature Trend (2000-2024)",
                  labels={'temperature': 'Temperature (°C)', 'date': 'Date'})
    
    fig.update_traces(line=dict(color='red', width=3))
    st.plotly_chart(fig, use_container_width=True)
    
    # Temperature statistics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Temperature Statistics")
        temp_stats = climate_data['temperature'].describe()
        st.dataframe(temp_stats)
    
    with col2:
        st.subheader("Annual Temperature Change")
        climate_data['year'] = climate_data['date'].dt.year
        annual_avg = climate_data.groupby('year')['temperature'].mean()
        annual_change = annual_avg.diff().dropna()
        
        fig_bar = px.bar(x=annual_change.index, y=annual_change.values,
                        title="Year-over-Year Temperature Change",
                        labels={'x': 'Year', 'y': 'Temperature Change (°C)'})
        st.plotly_chart(fig_bar, use_container_width=True)

elif page == "CO2 Levels":
    st.header("Atmospheric CO₂ Concentration")
    
    # CO2 trend chart
    fig = px.line(climate_data, x='date', y='co2_levels',
                  title="Atmospheric CO₂ Levels (2000-2024)",
                  labels={'co2_levels': 'CO₂ Concentration (ppm)', 'date': 'Date'})
    
    fig.update_traces(line=dict(color='blue', width=3))
    st.plotly_chart(fig, use_container_width=True)
    
    # CO2 vs Temperature correlation
    st.subheader("CO₂ vs Temperature Correlation")
    
    fig_scatter = px.scatter(climate_data, x='co2_levels', y='temperature',
                            trendline="ols",
                            title="CO₂ vs Temperature Relationship",
                            labels={'co2_levels': 'CO₂ (ppm)', 'temperature': 'Temperature (°C)'})
    
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # CO2 statistics
    st.subheader("CO₂ Statistics")
    co2_stats = climate_data['co2_levels'].describe()
    st.dataframe(co2_stats)

elif page == "Sea Level Rise":
    st.header("Global Sea Level Changes")
    
    # Sea level trend chart
    fig = px.line(climate_data, x='date', y='sea_level',
                  title="Global Sea Level Rise (2000-2024)",
                  labels={'sea_level': 'Sea Level Change (mm)', 'date': 'Date'})
    
    fig.update_traces(line=dict(color='green', width=3))
    st.plotly_chart(fig, use_container_width=True)
    
    # Sea level rise rate
    st.subheader("Sea Level Rise Rate")
    climate_data['sea_level_change'] = climate_data['sea_level'].diff()
    monthly_rise_rate = climate_data['sea_level_change'].mean()
    annual_rise_rate = monthly_rise_rate * 12
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Monthly Rise Rate", f"{monthly_rise_rate:.2f} mm/month")
    with col2:
        st.metric("Annual Rise Rate", f"{annual_rise_rate:.2f} mm/year")
    
    # Sea level statistics
    st.subheader("Sea Level Statistics")
    sea_stats = climate_data['sea_level'].describe()
    st.dataframe(sea_stats)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🌱 This dashboard demonstrates climate data visualization using simulated data</p>
    <p>Built with Streamlit • Data updated automatically</p>
</div>
""", unsafe_allow_html=True)
