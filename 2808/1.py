from typing import List

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        dict = {}
        ans = n
        for i,num in enumerate(nums):
            if num in dict:
                dict[num].append(i)
            else:
                dict[num] = [i]
        
        for pos in dict.values():
            maxlen = pos[0] - pos[-1] + n
            for i in range(len(pos)):
                maxlen = max(maxlen,pos[i]-pos[i-1])
            ans = min(ans,maxlen//2)
        return ans



