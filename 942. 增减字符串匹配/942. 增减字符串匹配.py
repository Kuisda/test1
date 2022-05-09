#如果是s[i]==I,使得ans[i]为当前可选的最小的数
#如果s[i]==D,使得ans[i]为当前可选的最大的数
#最大最小两个指针最终将指向同一个数，将这个数添加到ans中
from typing import List
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        left,right = 0,n
        ans = []
        for pos,ch in enumerate(s):
            if ch=='I':
                ans.append(left)
                left+=1
            elif ch=='D':
                ans.append(right)
                right-=1
        ans.append(left)
        return ans
