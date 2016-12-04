import pylab as lab

asset_items = [1258,640,772,13,63,78,161,289,60,282]
fracs = [round(each/sum(asset_items)*100,1) for each in asset_items]
labels = ['Cash','A/R','Inventories','GLOBF','Prepaid','Other Current','Property','Goodwill','Investments','Others']
colors =['#f26e6e','#6e7ef2','#6ed1f2','#f29d6e','#e1f26e','#b7f26e','#a46ef2','#f2ec6e','#6ef2a3','#51a0aa']
lab.axes(aspect =1)#cannot be put after pie function
lab.pie(fracs,labels = labels,colors = colors,autopct = '%.1f')#,startangle=100)

#[34.8, 17.7, 21.3, 0.4, 1.7, 2.2, 4.5, 8.0, 1.7, 7.8]



lab.show()
