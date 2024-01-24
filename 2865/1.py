from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        ans = 0
        preHeight = 0
        for i in range(len(maxHeights)):
            curSum = maxHeights[i]
            preHeight = maxHeights[i]
            for j in range(i-1,-1,-1):
                curHeight = maxHeights[j] if maxHeights[j]<= preHeight else preHeight
                curSum += curHeight
                preHeight = curHeight
            preHeight = maxHeights[i]
            for j in range(i+1,len(maxHeights)):
                curHeight = maxHeights[j] if maxHeights[j]<= preHeight else preHeight
                curSum += curHeight
                preHeight = curHeight
            ans =max(ans,curSum)
        return ans
    
c = Solution()
c.maximumSumOfHeights([6,5,3,9,2,7])