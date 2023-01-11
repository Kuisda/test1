from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        nums = list(map(lambda x:int(x),list(num)))
        dict = defaultdict()
        for _,ch in enumerate(nums):
            if ch not in dict:
                dict[ch]=1
            else:
                dict[ch]+=1
        n = len(nums)
        for i in range(n):
            if i not in dict:
                if nums[i]!=0:
                    return False
            elif nums[i]!=dict[i]:
                return False
        return True

c = Solution()
c.digitCount("1210")