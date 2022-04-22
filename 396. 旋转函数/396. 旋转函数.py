#找到F(k)与F(k-1)之间的关系
from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        numSum = sum(nums)
        F = 0
        for i in range(0,n):
            F+=i*nums[i]
        maxF = F
        for k in range(1,n):
            F = F+numSum-n*nums[n-k]
            maxF = max(F,maxF)
        return maxF
