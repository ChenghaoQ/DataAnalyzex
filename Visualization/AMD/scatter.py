import matplotlib.pyplot as plt
from matplotlib.dates import bytespdates2num
date,high,low=lab.loadtxt('Nov21-1yr.csv',delimiter = ',',converters ={0:bytespdates('%Y-%m-%d')},skiprows =1,usecols=(0,2,3),unpack=True)

diff = high - low


lab.scatter(date,diff)
lab.show()
