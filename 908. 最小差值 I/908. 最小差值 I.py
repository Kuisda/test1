from typing import List
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-1]-nums[0]-2*k if nums[-1]-nums[0]-2*k>0 else 0
