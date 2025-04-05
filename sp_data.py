import yfinance as yf
import pandas as pd

# Step 1: Download historical S&P 500 data (ticker: ^GSPC)
sp500_raw = yf.download("^GSPC", start="2018-01-01", end="2023-01-01")

# Step 2: Flatten the MultiIndex by resetting columns
sp500_raw.columns = ['_'.join(col).strip() for col in sp500_raw.columns.values]

# Step 3: Keep only necessary columns (flattened names)
sp500 = sp500_raw[["Open_^GSPC", "High_^GSPC", "Low_^GSPC", "Close_^GSPC", "Volume_^GSPC"]].copy()

# Step 4: Calculate Daily % Change based on Close
sp500["Pct_Change"] = sp500["Close_^GSPC"].pct_change() * 100

# Step 5: Drop the first row with NaN in % change
sp500.dropna(inplace=True)

# Step 6: Reset index to make 'Date' a column
sp500.reset_index(inplace=True)

# Step 7: Preview cleaned data
print(sp500.head())

# Step 8: Save to CSV
sp500.to_csv("sp500_cleaned_2018_2023.csv", index=False)
