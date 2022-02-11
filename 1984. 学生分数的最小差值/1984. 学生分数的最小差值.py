from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort(key = lambda x:-x)
        ans = float("inf")
        for i in range(0,len(nums)-k+1):
            if ans > nums[i]-nums[i+k-1]:
                ans = nums[i]-nums[i+k-1]
        return ans