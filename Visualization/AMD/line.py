import pylab as lab

date,close=lab.loadtxt('Nov21-1yr.csv',delimiter = ',',converters = {0:lab.strpdate2num('%M-%D-%Y')},skiprows =1,usecols=(0,4),unpack=True)
lab.plot(date,close)

lab.show()
