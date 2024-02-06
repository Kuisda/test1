import heapq
from typing import List
#if current sum <= 0(assume current pos i) , turn the lowest num to the behind in nums[0]~nums[i] 
#use min heap for implementation
class Solution:
    def magicTower(self, nums: List[int]) -> int:
        adjust,delay,sum = 0,0,1#adjust time,delay represent the sum of numbers turn behind
        p = []
        for num in nums:
            if num < 0:
                heapq.heappush(p,num)#min heap
            sum += num
            if sum <= 0:
                adjust += 1
                sum -= p[0]
                delay += heapq.heappop(p)
        sum += delay
        return -1 if sum <= 0 else adjust

c = Solution()
c.magicTower([100,100,100,-250,-60,-140,-50,-50,100,150])
