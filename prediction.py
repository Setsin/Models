import pandas as pd
from pandas import Series
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults

data = pd.read_series('./data/BTC-USD(PB).csv') 
model_load = ARIMAResults.load('./models/ARIMA BTC-USD AR')

print(model_load)