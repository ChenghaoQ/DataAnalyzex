import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import bytespdate2num
date,high,low=np.loadtxt('Nov21-1yr.csv',delimiter = ',',converters ={0:bytespdate2num('%Y-%m-%d')},skiprows =1,usecols=(0,2,3),unpack=True)

diff = high - low

plt.scatter(date,diff,alpha = 0.4)
plt.show()
