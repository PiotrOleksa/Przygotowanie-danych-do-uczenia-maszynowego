import pandas as pd
import altair as alt
import yfinance as yf
import matplotlib.pyplot as plt


tsla = yf.Ticker("TSLA")
df = tsla.history(period='max')
df = df[-253:]
df = df.drop(['High', 'Low', 'Open', 'Volume', 'Dividends', 'Stock Splits'], axis=1)


df['SMA_7'] = df['Close'].rolling(7).mean()
df['SMA_21'] = df['Close'].rolling(21).mean()

fig, ax = plt.subplots()
df.plot(figsize=(15,15), ax=ax)
ax.legend(['Close Price', 'SMA 7', 'SMA 21'])

df['Date'] = df.index
Close = alt.Chart(df).mark_line().encode(
    x='Date',
    y='Close'
).properties(
    width=800,
    height=800
)

SMA_7 = alt.Chart(df).mark_line(color='orange').encode(
    x='Date',
    y='SMA_7'
).properties(
    width=800,
    height=800
)

SMA_21 = alt.Chart(df).mark_line(color='green').encode(
    x='Date',
    y='SMA_21',
).properties(
    width=800,
    height=800
)
alt_plot = Close + SMA_7 + SMA_21
alt_plot.interactive()