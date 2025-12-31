# Market Data Analytics Dashboard

Interactive dashboard for visualizing market data from AWS RDS PostgreSQL database.

## Features
- Interactive candlestick price charts
- Volume analysis
- Real-time ticker data querying
- Summary statistics (latest close, average, high, low)
- Adjustable data range (100-5000 records)

## Tech Stack
- **Python** - Core programming language
- **Streamlit** - Web dashboard framework
- **Plotly** - Interactive charting library
- **PostgreSQL** - AWS RDS database
- **pandas** - Data manipulation

## Setup

1. Clone the repository:
```bash
   git clone https://github.com/ogadegun/market-data-dashboard.git
   cd market-data-dashboard
```

2. Create virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Configure database connection:
   - Copy `db_connection_template.py` to `db_connection.py`
   - Update with your AWS RDS credentials

5. Run the dashboard:
```bash
   streamlit run dashboard.py
```

6. Open browser to `http://localhost:8501`

## Usage

- Enter ticker symbol in sidebar (e.g., AAPL, GOOGL, MSFT)
- Adjust number of records using slider
- View interactive candlestick chart and volume data
- Expand "View Raw Data" to see underlying data table

## Screenshots
(Add screenshots after deploying)

## Project Structure
```
market-data-dashboard/
├── dashboard.py              # Main Streamlit application
├── db_connection_template.py # Database connection template
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```
