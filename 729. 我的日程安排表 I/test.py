from bisect import bisect_left
from sortedcontainers import SortedDict

dict = SortedDict({1:3,4:7,10:12})
index = dict.bisect_left(6)
#index = 2
#SortedDict只保证key是有序且可比较的，所以bisect_left其实也只能对key序列二分查找
print(index)