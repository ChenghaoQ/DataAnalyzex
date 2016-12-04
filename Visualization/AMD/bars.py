import matplotlib.pyplot as plt
import numpy as np

N = 4
y_revenue = [958,832,1207,1307]
x_namepos =np.subtract(np.arange(4)*1.5,0.5) 


x = np.arange(N)*1.5
plt.bar(left=x,height=y_revenue,color ='#51ADD8',width=0.5,align='center')



x_namepos =np.arange(4)*1.5
x_date=['12/26/2015','3/26/2016','6/25/2016','9/24/2016']
plt.xticks(x_namepos,x_date)
plt.show()

