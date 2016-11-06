def maxVal(toConsider,avail):
        
        if toConsider == [] or avail ==0:
                result = (0,())
        elif toConsider[0].getCost() > avail:
                result = maxVal(toConsider[1:],avail)
        else:
                nextItem = toConsider[0]
                withVal,withToTake = maxVal(toConsider[1:],avail - nextItem.getCost())
                withVal += nextItem.getValue()
                withoutVal,withoutToTake = maxVal(toConsider[1:],avail)
                if withVal > withoutVal:
                        result = (withVal,withToTake + (nextItem,))
                else:
                        result = (withoutVal,withoutToTake)
        return result

def fastmaxVal(toConsider,avail,memo= {}):
        if (len(toConsider),avail) in memo:
                result = memo[(len(toConsider),avail)]
        elif toConsider == [] or avail == 0:
                result = (0,())
        elif toConsider[0].getCost() > avail:
                result = fastmaxVal(toConsider[1:],avail,memo)
        else:
                nextItem = toConsider[0]

                #Explore left branch
                withVal,withToTake = fastmaxVal(toConsider[1:],avail - nextItem.getCost(),memo)
                withVal += nextItem.getValue()
                #Explore right branch
                withoutVal,withoutToTake = fastmaxVal(toConsider[1:],avail,memo)
                if withVal > withoutVal:
                        result = (withVal,withToTake + (nextItem,))
                else:
                        result = (withoutVal, withoutToTake)

        memo[(len(toConsider),avail)] = result
        return result

def testMaxVal(foods,maxUnits,printItems = True):

        print("Use search tree to allocate",maxUnits,'calories')
        val,taken = fastmaxVal(foods,maxUnits)
        print('Total value of item taken =',val)
        if printItems:
                for item in taken:
                        print('   ',item)


