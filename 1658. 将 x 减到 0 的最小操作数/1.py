from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left,right =-1,0
        total = sum(nums)
        step  = n+1 #初值设为n+1是为了面对sum(nums)>x的情况

        if total<x:
            return -1
        while left<n-1:#永远不会导致left在right的右边，因为left = right-1的时候，total ==sum(nums)，必将导致right右移
            while right<n and total>x:
                total-=nums[right]
                right+=1
            if total==x:
                step = min(step,(n-right)+(left+1))
            left+=1
            total+=nums[left]
        return -1 if step>n else step
