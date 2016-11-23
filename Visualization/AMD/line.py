import pylab as lab


def bytedate2num(fmt):
    def converter(b):
        return lab.strpdate2num(fmt)(b.decode('ascii'))
    return converter

date,close=lab.loadtxt('Nov21-1yr.csv',delimiter = ',',converters = {0:bytedate2num('%Y-%m-%d')},skiprows =1,usecols=(0,4),unpack=True)
lab.plot(date,close)

lab.show()
