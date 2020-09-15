from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table
import pandas as pd

# Dataset all-data (+ Rename first column )
BTC = get_data("BTC-USD")
df = pd.DataFrame(BTC, index=None)
df.rename(columns={'Unnamed: 0':'Date'}, inplace=True)
df.to_csv(path_or_buf="./data/BTC-USD.csv")

df.to_csv(path_or_buf="./data/BTC-USD.csv")

# Dataset post-bullrun 2017

post_bull = get_data('BTC-USD', start_date = "21-06-2018")
df2 = pd.DataFrame(post_bull)
df2.rename(columns={'Unnamed: 0':'Date'}, inplace=True)
df2.to_csv(path_or_buf="./data/BTC-USD(PB).csv")
print(df2['Date'])