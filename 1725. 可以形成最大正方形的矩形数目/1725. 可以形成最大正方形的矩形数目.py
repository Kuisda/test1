from sortedcontainers import SortedList
from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLenList = SortedList()

        for l,w in rectangles:
            maxLenList.add(min(l,w))
        ans = 0
        maxLen = maxLenList[-1] 
        for num in reversed(maxLenList):
            if num == maxLen:
                ans+=1
            else:
                break
        return ans

class Solution2:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        maxLen = 0
        for l,w in rectangles:
            lower = min(l,w)
            if lower>maxLen:
                ans = 1
                maxLen = lower
            elif lower==maxLen:
                ans+=1
        return ans        


x = Solution()
print(x.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))