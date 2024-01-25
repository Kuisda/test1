from typing import List
class Solution:
    def Bit_count(self,num:int )->int:
        ans = 0
        while num !=0:
            if num & 1 == 1:
                ans +=1
            num = num >>1
        return ans
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i,num in enumerate(nums):
            if self.Bit_count(i) == k:
                ans += num
        return ans

c = Solution()
c.sumIndicesWithKSetBits([5,10,1,5,2],1)