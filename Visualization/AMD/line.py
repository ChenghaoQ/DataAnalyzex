import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import bytespdate2num

date,close=np.loadtxt('Nov21-1yr.csv',delimiter = ',',converters = {0:bytespdate2num('%Y-%m-%d')},skiprows =1,usecols=(0,4),unpack=True)


spopen,spclose=np.loadtxt('Nov21-1yr-SP500.csv',delimiter = ',',skiprows =1,usecols=(1,4),unpack=True)
spchanges = np.divide(spclose-spopen,spopen)

def sp500_scale_down(close_price,changes):
	stdsp = []
	for each in changes:
		close_price = close_price*(1+each)
		stdsp.append(close_price)

	return np.array(stdsp)

stdsp = sp500_scale_down(close[-1]/(1+spchanges[-1]),spchanges[::-1])

plt.plot_date(date,close,linestyle='-',markersize =2.5,color='#147FB1',label='AMD')
plt.plot_date(date,stdsp[::-1],linestyle='-',markersize =2.5,color='#14B158',label='S&P500')
plt.legend(loc = 'upper left')

plt.show()




