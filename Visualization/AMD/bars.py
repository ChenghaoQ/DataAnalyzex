import pylab as lab

N = 4
y_revenue = [1307,1207,832,958]
x_namepos =lab.subtract(lab.arange(4)*1.5,0.5) 


x = lab.arange(N)*1.5
lab.bar(left=x,height=y_revenue,color ='red',width=0.5,align='center')



x_namepos =lab.arange(4)*1.5
x_date=['12/26/2015','3/26/2016','6/25/2016','9/24/2016']
lab.xticks(x_namepos,x_date)
lab.show()

