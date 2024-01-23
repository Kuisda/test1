from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        i,j = 0,0
        maxlen = 0
        curincrement = 1
        while 1:
            j+=1
            if j == len(nums):
                break
            if nums[j]-nums[j-1] == curincrement:
                maxlen = max(maxlen,j-i+1)
                curincrement = -curincrement
            elif nums[j] - nums[j-1] == 1:
                i = j-1
                curincrement = -1
            else:
                i = j
                curincrement = 1
        return maxlen if maxlen>0 else -1
    

c = Solution()
c.alternatingSubarray([2,3,4,3,4])

