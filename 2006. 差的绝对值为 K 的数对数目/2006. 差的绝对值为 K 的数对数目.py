from typing import List
from collections import Counter
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    ans+=1

        return ans

#使用哈希表
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = Counter()
        for num in nums:
            res += cnt[num - k] + cnt[num + k]
            cnt[num] += 1
        return res

  