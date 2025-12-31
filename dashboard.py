import streamlit as st
import plotly.graph_objects as go
from db_connection import query_ticker_data

st.set_page_config(page_title="Market Data Dashboard", layout="wide")

st.title("📈 Market Data Analytics Dashboard")
st.markdown("Interactive visualization of market data from AWS RDS")

# Sidebar for inputs
st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Enter Ticker Symbol", "AAPL").upper()
data_limit = st.sidebar.slider("Number of Records", 100, 5000, 1000)

# Fetch data
with st.spinner(f"Loading data for {ticker}..."):
    df = query_ticker_data(ticker, data_limit)

if not df.empty:
    # Display data info
    st.success(f"Loaded {len(df)} records for {ticker}")
    
    # Candlestick chart
    st.subheader(f"{ticker} Price Chart")
    fig = go.Figure(data=[go.Candlestick(
        x=df['timestamp'],
        open=df['open_price'],
        high=df['high_price'],
        low=df['low_price'],
        close=df['close_price'],
        name=ticker
    )])
    
    fig.update_layout(
        title=f"{ticker} Candlestick Chart",
        yaxis_title="Price ($)",
        xaxis_title="Time",
        template="plotly_white",
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Volume chart
    st.subheader(f"{ticker} Volume")
    volume_fig = go.Figure(data=[go.Bar(
        x=df['timestamp'],
        y=df['volume'],
        name='Volume'
    )])
    
    volume_fig.update_layout(
        title=f"{ticker} Trading Volume",
        yaxis_title="Volume",
        xaxis_title="Time",
        template="plotly_white",
        height=400
    )
    
    st.plotly_chart(volume_fig, use_container_width=True)
    
    # Basic statistics
    st.subheader("Summary Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Latest Close", f"${df['close_price'].iloc[0]:.2f}")
    with col2:
        st.metric("Avg Price", f"${df['close_price'].mean():.2f}")
    with col3:
        st.metric("High", f"${df['high_price'].max():.2f}")
    with col4:
        st.metric("Low", f"${df['low_price'].min():.2f}")
    
    # Show raw data (optional)
    with st.expander("View Raw Data"):
        st.dataframe(df)
        
else:
    st.error(f"No data found for ticker: {ticker}")
    st.info("Try a different ticker symbol (e.g., AAPL, GOOGL, MSFT)")