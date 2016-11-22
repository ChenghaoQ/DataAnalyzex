import pylab as lab

high,low=lab.loadtxt('Nov21-1yr.csv',delimiter = ',',skiprows =1,usecols=(2,3),unpack=True)
changes = high - low
yesterday = changes[1:]
today = changes[:-1]
lab.scatter(yesterday,today)
lab.show()
