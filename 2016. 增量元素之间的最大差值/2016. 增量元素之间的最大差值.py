from typing import List
#维护nums[0...j-1]中的最小值，对j遍历，用j减去前缀的最小值就可以遍历到所有可能的最大差值
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        prenum=nums[0]
        ans=-1
        for i in range(1,len(nums)):
            if nums[i]>prenum:
                ans = max(ans,nums[i]-prenum)
            else:
                prenum = nums[i]
        return ans            

