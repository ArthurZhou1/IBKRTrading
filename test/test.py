# from ib_insync import *
# # util.startLoop()  # uncomment this line when in a notebook

# ib = IB()
# ib.connect('127.0.0.1', 7497, clientId=1)

# contract = Crypto('BTC', 'PAXOS', 'USD')
# bars = ib.reqHistoricalData(
#     contract, endDateTime='', durationStr='30 D',
#     barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# # convert to pandas dataframe (pandas needs to be installed):
# df = util.df(bars)
# print(df)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()