import matplotlib.pyplot as plt
import numpy as np
N = 4
x = np.arange(N)*1.5
revenue = [958,832,1207,1307]
income = [-102,-109,69,-406]
plt.bar(left=x,height=revenue,color ='#D85B51',width=0.5,alpha = 0.75,align='center',label="Revenue")
plt.bar(left=x+0.5,height=income,color ='#51ADD8',width=0.5,alpha=0.75,align='center',label="Net Income")

plt.legend(loc = 'upper left')
x_datepos =np.add(np.arange(4)*1.5,0.25)
x_date=['12/26/2015','3/26/2016','6/25/2016','9/24/2016']
plt.xticks(x_datepos,x_date)
plt.show()



