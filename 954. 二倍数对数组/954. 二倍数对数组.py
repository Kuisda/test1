from typing import List
from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        if cnt[0]%2:    #判断0的数量，如果为奇数则不能配对
            return False
        for x in sorted(cnt,key=abs):#正负等价，在排序的时候 -2,2会在相邻位置
            if cnt[2*x] <cnt[x]: #按照键值从小到大排序，最小键值的数只能和其两倍2*x来配对，如果2*x数的个数小于x的个数则必定有x没有配对
                return False      
            cnt[2*x]-=cnt[x]     #减去与x配对的2*x的数量
        return True





x = Solution()
x.canReorderDoubled([4,-2,2,-4])