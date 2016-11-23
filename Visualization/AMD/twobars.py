import pylab as lab

N = 4
x = lab.arange(N)*1.5
revenue = [958,832,1207,1307]
income = [-102,-109,69,-406]
lab.bar(left=x,height=revenue,color ='red',width=0.5,alpha = 0.75)
lab.bar(left=x+0.5,height=income,color ='blue',width=0.5,alpha=0.75)

x_datepos =lab.add(lab.arange(4)*1.5,0.5)
x_date=['12/26/2015','3/26/2016','6/25/2016','9/24/2016']
lab.xticks(x_datepos,x_date)
lab.show()



