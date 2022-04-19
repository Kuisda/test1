#两侧遍历，分别求所有位置距左侧最近c的距离以及距右侧最近c的距离，如果左侧或者右侧没有，对应距离为无限大
from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0]*n
        
        idx = -n   #主要目的是在没有左侧的c字符时，距离左侧c字符的距离为无穷大(大于任何一个长度)
        for i,ch in enumerate(s):
            if ch==c:
                idx = i
            ans[i] = i - idx 

        idx = n*2
        for i in range(n-1,-1,-1): #[n-1,-1)
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i],idx-i)
        return ans
            
