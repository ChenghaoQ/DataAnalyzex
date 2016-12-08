'''Suppose the spaceship has a weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The greedy algorithm will first pick Jesse as the heaviest cow for the first trip. There is still space for 4 tons on the trip. Since Maggie will not fit on this trip, the greedy algorithm picks Maybel, the heaviest cow that will still fit. Now there is only 1 ton of space left, and none of the cows can fit in that space, so the first trip is [Jesse, Maybel].

For the second trip, the greedy algorithm first picks Maggie as the heaviest remaining cow, and then picks Callie as the last cow. Since they will both fit, this makes the second trip [[Maggie], [Callie]].

The final result then is [["Jesse", "Maybel"], ["Maggie", "Callie"]].'''
{"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}


class Cow(object):
	def __init__(self,n,w):
		self.name = n
		self.weight = w
	def getWeight(self):
		return self.weight
	def getName(self):
		return self.name
	
def greedy_cow_transport(cows,limit=10):
	cowlist=[]
	for each in cows.keys():
		cowlist.append(Cow(each,cows[each]))
	
	 
	cowlistCopy = sorted(cowlist, key = Cow.getWeight, reverse = True)
	
	totalweight = 0.0
	entirelist=[]
	result=[]
	i = 0
	while cowslistCopy:
		
		if(totalweight + cowlistCopy[i].getWeight()) <= limit and len(cowslistCopy)>1:
			result.append(cowslistCopy[i].getName)
			totalweight+= cowslistCopy.getweight()
			cowslist.pop(i)
			i-=1	
		else:
			entirelist.append(result[:])
			result=[]
			i=0
			totalweight=0
		i+=1

	return  entirelist
