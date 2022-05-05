from typing import List
from math import log
from bisect import bisect_right
#滑动窗口
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        prod = 1
        i = 0
        for j,num in enumerate(nums):
            prod*=num
            while i<=j and prod>=k:
               prod //=nums[i]
               i+=1
            ans +=j-i+1
        return ans

#对乘积取对数，然后记录前缀和数组，对前缀和数组的右端点进行遍历，二分查找得到第一个小于(右端点-目标值的对数logk)的位置
class Solution1:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        ans,n = 0,len(nums)
        logK = log(k)
        logNums = [0]*(n+1)
        for i,num in enumerate(nums):
            logNums[i+1] = logNums[i] + log(num)
        for j in range(1,n+1):
            l = bisect_right(logNums,logNums[j]-logK+1e-10,0,j)#1e-10用来避免误差，double类型只能保证前15位是精确的
            ans +=j-l
        return ans

