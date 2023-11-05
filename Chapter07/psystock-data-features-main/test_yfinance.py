import yfinance as yf

df = yf.download('BTC-USD')
print(df.head())

# Define the ticker symbol
tickerSymbol = 'BTC-USD'

# Define the start and end dates
startDate = '2020-01-01'
endDate = '2023-01-01'

# Get the data
data = yf.download(tickerSymbol, start=startDate, end=endDate)

# Print the first few rows of the data
print(data.head())
