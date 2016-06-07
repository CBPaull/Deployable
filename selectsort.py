rolls = input('Number of values: ')
from datetime import datetime
startTime = datetime.now()
rollist = []
for count in range (0, rolls):
	import random
	var = random.random()*10000
	roundvar = round(var)
	rollist.append(roundvar)
for i in range(len(rollist)):
    mini = min(rollist[i:]) #find minimum element
    min_index = rollist[i:].index(mini) #find index of minimum element
    rollist[i + min_index] = rollist[i] #replace element at min_index with first element
    rollist[i] = mini             
print rollist


print datetime.now() - startTime









