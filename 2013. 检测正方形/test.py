from collections import defaultdict
from collections import Counter
dict = defaultdict(list)
dict[0].append(1)
dict[0].append(1)
#dict[1][2] = 1
print(dict)

dic = defaultdict(Counter)

dic[1][2]=1
print(dic)


colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print (c)