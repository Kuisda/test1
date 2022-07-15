from typing import List
#以左指针i为主向右遍历，然后再考虑j
class Solution:
    def findPairs(self, nums: List[int], k: int) :
        ans = 0
        n = len(nums)
        nums.sort()
        i,j=0,0
        for i in range(n):
            if i==0 or nums[i] !=nums[i-1]:
                while j<n and (nums[j]<nums[i]+k or j<=i):
                    j+=1
                if j<n and nums[j] == nums[i]+k:
                    ans+=1
        return ans

x = Solution()
x.findPairs([3,1,4,1,5],2)