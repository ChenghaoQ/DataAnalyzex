import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

N = 4
y_revenue = [958,832,1207,1307]
y_namepos =np.subtract(np.arange(4)*1.5,0.5) 


y = np.arange(N)*1.5
plt.barh(left = 0,bottom=y,height=0.5,color ='#51ADD8',width=y_revenue,align='center')



x_namepos =np.arange(4)*1.5
x_date=['12/26/2015','3/26/2016','6/25/2016','9/24/2016']
plt.yticks(x_namepos,x_date)
plt.show()
