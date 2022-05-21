from typing import List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ss = set()
        for i,num in enumerate(nums):
            if num not in ss:
                ss.add(num)
            else:
                return num