import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller


bc = pd.read_csv('./Data/BTC-USD.csv')

# Ajout d'un nom pour la col 'date' et Convertion en datetime
bc.rename(columns={'Unnamed: 0':'Date'}, inplace=True)

bc['Date'] = pd.to_datetime(bc.Date)

# Setting the index as the dates

bc.set_index(bc['Date'], inplace=True)

print(bc)
# Selecting only the dates from 2017-01-01 onwards
bc = bc[['close']].loc['2017-01-01':]

# Converting the data to a logarithmic scale
bc_log = pd.DataFrame(np.log(bc.close))

# Differencing the log values
log_diff = bc_log.diff().dropna()

# Using the Dickey-Fuller test to check for stationarity
results = adfuller(log_diff.close)
print(f"P-value: {results[1]}")