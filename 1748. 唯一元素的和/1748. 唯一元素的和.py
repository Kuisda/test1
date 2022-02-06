from typing import List
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        nums_set = {}
        for num in nums:
            if num not in nums_set:
                ans+=num
                nums_set[num] = 1
            elif num in nums_set and nums_set[num]==1:
                ans-=num
                nums_set[num] =0
        return ans            

x = Solution()
sum = x.sumOfUnique([1,2,3,2])