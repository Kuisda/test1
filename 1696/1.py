from typing import List

#first step is nums[0]
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = [[0,nums[0]]]
        ans = nums[0]
        for i in range(1,n):
            if queue[0][0] < i-k:
                queue.pop(0)
            curVal = queue[0][1] + nums[i]
            if i == n-1:
                ans = curVal
            while queue and curVal >= queue[-1][1]:
                queue.pop(-1)
            queue.append([i,curVal])
        return ans


