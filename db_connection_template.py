import psycopg2
import pandas as pd

def get_connection():
    """Connect to AWS RDS PostgreSQL database"""
    return psycopg2.connect(
        host="your-rds-endpoint.rds.amazonaws.com",
        database="your-database-name",
        user="your-username",
        password="your-password",
        port=5432
    )

def query_ticker_data(ticker, limit=1000):
    """Query market data for a specific ticker"""
    conn = get_connection()
    query = """
        SELECT timestamp, open_price, high_price, low_price, close_price, volume
        FROM market_data
        WHERE ticker = %s
        ORDER BY timestamp DESC
        LIMIT %s
    """
    df = pd.read_sql(query, conn, params=(ticker, limit))
    conn.close()
    return df
