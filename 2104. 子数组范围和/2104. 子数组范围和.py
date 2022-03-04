from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        sum = 0
        n = len(nums)
        for i in range(n):
            minVal,maxVal = float('inf'),-float('inf')
            for j in range(i,n):
                minVal = min(minVal,nums[j])
                maxVal = max(maxVal,nums[j])
                sum+=maxVal-minVal

        return sum

