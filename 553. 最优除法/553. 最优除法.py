import enum
from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        ans=""
        n = len(nums)
        if n==1:
            return str(nums[0])
        if n==2:
            return ans+str(nums[0])+'/'+str(nums[1])    
        for i,num in enumerate(nums):
            if i!=0:
                ans+='/'
            if i==1:
                ans+='('    
            ans+=str(num)
        ans+=')'
        return ans 