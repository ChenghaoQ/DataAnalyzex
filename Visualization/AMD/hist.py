import matplotlib.pyplot as plt
import numpy as np

open_price,close_price=np.loadtxt('Nov21-1yr.csv',delimiter = ',',skiprows =1,usecols=(1,4),unpack=True)
diff = ((close_price-open_price)/open_price)*100

plt.hist(diff,bins=30,color='#EA4545',normed=True)

plt.show()


