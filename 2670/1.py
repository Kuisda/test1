from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff = []
        dictBefore = {}
        dictAfter = {}
        n = len(nums)
        for num in nums:
            if num in dictAfter:
                dictAfter[num] +=1
            else:
                dictAfter[num] = 1
        for i in range(n):
            if nums[i] in dictBefore:
                dictBefore[nums[i]] +=1
            else:
                dictBefore[nums[i]] = 1
            dictAfter[nums[i]] -=1
            if dictAfter[nums[i]] == 0:
                dictAfter.pop(nums[i])
            dif = len(dictBefore) - len(dictAfter)
            diff.append(dif)
        return diff

c = Solution()
print(c.distinctDifferenceArray([3,2,3,4,2]))