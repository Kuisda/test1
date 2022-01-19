import enum
from typing import List

def takesecond(elem):
    return elem[1]

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = []
        for i in range(len(nums)):
            temp = [i,nums[i]]
            hash.append(temp)
        hash.sort(key=takesecond)

        for i in range(len(hash)-1):
            if(hash[i][1]==hash[i+1][1] and abs(hash[i][0]-hash[i+1][0])<=k):
                return True
        return False        

#哈希表,数据num:i,每次更新i为num最新的位置
def method2(self, nums: List[int], k: int) ->bool:
    hashmap = {}
    for i,num in enumerate(nums):
        if num in hashmap and i-hashmap[num]<=k:
            return True
        hashmap[num] = i     
    return False

#滑动窗口，窗口长度为k，每当长度大于k时每次去掉最前的一位
def method3(self, nums: List[int], k: int) ->bool:
    s = set()
    for i,num in enumerate(nums):
        if i>k:
            s.remove(nums[i-k-1])
        if num in s:
            return True
        s.add(num)
    return False        