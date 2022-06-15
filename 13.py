from heapq import nlargest
from operator import itemgetter
items = {'India': 45.50, 'America':35, 'China': 41.30, 'Australia':55, 'Europe': 24, 'Dubai': 27}
for name, value in nlargest(5, items.items(), key=itemgetter(1)):
    print(name, value)
	