# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import warnings
from itertools import product
from datetime import datetime


warnings.filterwarnings('ignore')
plt.style.use('seaborn-poster')


# %%
btc = pd.read_csv('./Data/BTC-USD.csv')


# %%
# Ajout d'un nom pour la col 'Date' et Convertion en datetime et index

btc.rename(columns={'Unnamed: 0':'Date'}, inplace=True)
btc['Date'] = pd.to_datetime(btc.Date)


# %%
#Set Date as Index
btc.set_index('Date', inplace=True)


# %%
# Selecting only the dates from 2017-01-01 onwards when Bitcoin popularity increased.
#btc = btc[['close']].loc['2017-01-01':]


# %%
# Converting the data to a logarithmic scale
btc_log = pd.DataFrame(np.log(btc.close))

btc_log.plot()


# %%
# Differencing the log values
log_diff = btc_log.diff().dropna()
log_diff.plot()


# %%
#ACF (Auto Correlation Function)
plot_acf(log_diff)


# %%
#PACF (Partial Autocorrelation Function)
plot_pacf(log_diff, lags=50)


# %%
# Resampling to daily frequency
btc = btc.resample('D').mean()


# %%
# Resampling to monthly frequency
btc_month = btc.resample('M').mean()


# %%
# Resampling to annual frequency
btc_year = btc.resample('A-DEC').mean()


# %%
# Resampling to quarterly frequency
btc_Q = btc.resample('Q-DEC').mean()


# %%
print(btc_Q)


# %%
# PLOTS Daily / Months / Quarters / Years
fig = plt.figure(figsize=[15, 7])
plt.suptitle('Bitcoin exchanges, mean USD', fontsize=22)

plt.subplot(221)
plt.plot(btc.adjclose, '-', label='By Days')
plt.legend()

plt.subplot(222)
plt.plot(btc_month.adjclose, '-', label='By Months')
plt.legend()

plt.subplot(223)
plt.plot(btc_Q.adjclose, '-', label='By Quarters')
plt.legend()

plt.subplot(224)
plt.plot(btc_year.adjclose, '-', label='By Years')
plt.legend()

# plt.tight_layout()
plt.show()


# %%
plt.figure(figsize=[15,7])
sm.tsa.seasonal_decompose(btc_month.adjclose).plot()
print("Dickey–Fuller test: P-value = %f" % sm.tsa.stattools.adfuller(btc_month.adjclose)[1])
plt.show()


# %%
#Observation : la serie n'est pas stationnaire


# %%
# Box-Cox Transformations

btc_month['adjclose_box'], lmbda = stats.boxcox(btc_month.adjclose)
print("Dickey–Fuller test: p=%f" % sm.tsa.stattools.adfuller(btc_month.adjclose)[1])
plt.show()


# %%
# Seasonal differentiation
btc_month['adjclose_box_diff'] = btc_month.adjclose_box - btc_month.adjclose_box.shift(12)
print("Dickey–Fuller test: p=%f" % sm.tsa.stattools.adfuller(btc_month.adjclose_box_diff[12:])[1])


# %%
# Regular differentiation
btc_month['adjclose_box_diff2'] = btc_month.adjclose_box_diff - btc_month.adjclose_box_diff.shift(1)
plt.figure(figsize=(15,7))

# STL-decomposition
sm.tsa.seasonal_decompose(btc_month.adjclose_box_diff2[13:]).plot()   
print("Dickey–Fuller test: p=%f" % sm.tsa.stattools.adfuller(btc_month.adjclose_box_diff2[13:])[1])

plt.show()


# %%
#Observation : La série est stationnaire


# %%



# %%



# %%



