from typing import List

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        s,n = sum(beans),len(beans)
        return min(s - x *(n-1) for i,x in enumerate(beans))


c = Solution()
c.minimumRemoval([4,1,6,5])