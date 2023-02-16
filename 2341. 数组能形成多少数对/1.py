from typing import List
from collections import defaultdict
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dict = defaultdict()
        count = 0
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] -=1
                if dict[num] == 0:
                    count += 1
                    del dict[num]
        return [count,len(nums)-count*2]
    
x = Solution()
x.numberOfPairs([1,3,2,1,3,2,2])
                