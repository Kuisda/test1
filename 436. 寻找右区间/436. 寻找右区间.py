from typing import List
from bisect import bisect_left
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i,interval in enumerate(intervals):
            interval.append(i)
        
        intervals.sort(key=lambda x:x[0])

        n = len(intervals)
        ans = [-1]*n

        for i in range(n):
           pos = bisect_left(intervals,[intervals[i][1]]) #这样二分查找的标准是每一个[a,b,c]三元列表的第一项

           if pos < n:
               ans[intervals[i][2]] = intervals[pos][2]
        return ans
x = Solution()
x.findRightInterval([[3,4],[2,3],[1,2]])