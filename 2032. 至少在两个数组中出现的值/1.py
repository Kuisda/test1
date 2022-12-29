from collections import defaultdict
from typing import List
class Solution(object):
    def twoOutOfThree(self, nums1:List[int], nums2:List[int], nums3:List[int])->List[int]:
        nums1.sort()
        nums2.sort()
        nums3.sort()
        ans = set()
        i,j,k=0,0,0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]==nums2[j]:
                ans.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        i,j=0,0
        while(i<len(nums1) and k<len(nums3)):
            if nums1[i] == nums3[k]:
                ans.add(nums1[i])
                i+=1
                k+=1
            elif nums1[i]<nums3[k]:
                i+=1
            else:
                k+=1
        i,k=0,0
        while(j<len(nums2) and k<len(nums3)):
            if nums2[j]==nums3[k]:
                ans.add(nums2[j])
                j+=1
                k+=1
            elif nums2[j]<nums3[k]:
                j+=1
            else:
                k+=1
        return list(ans)


def answer(self, nums1:List[int], nums2:List[int], nums3:List[int])->List[int]:
    #直接用集合的逻辑运算来做就行了
    return list(
            (set(nums1) & set(nums2)) | 
            (set(nums1) & set(nums3)) | 
            (set(nums2) & set(nums3))
        )

#使用哈希表+位运算的方法
#键值对分别存（数组中的数据：出现在的组），组这个部分就用位运算表示，比如101就表示出现在组1和组3
def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    mask = defaultdict(int)
    for i, nums in enumerate((nums1, nums2, nums3)):
        for x in nums:
            mask[x] |= 1 << i
    return [x for x, m in mask.items() if m & (m - 1)]






c = Solution()
nums1 = [1,1,3,2]
nums2 = [2,3] 
nums3 = [3]
print(c.twoOutOfThree(nums1,nums2,nums3))