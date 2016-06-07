
rolls = input('Number of values: ')
rollist = []
for count in range (0, rolls):
	import random
	var = random.random()*10000
	roundvar = round(var)
	rollist.append(roundvar)
sort = False  
while not sort:
	sort = True
	for element in range(0, rolls-1):
		if rollist[element] > rollist[element + 1]:
			sort = False  # We found two elements in the wrong order
			rollist[element], rollist[element+1] = rollist[element+1], rollist[element]
print rollist








