from typing import List
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        r = [0]*m
        c = [0]*n
        ans=0
        for x,y in indices:
            r[x]+=1
            c[y]+=1
        for i in range(m):
            for j in range(n):
                if (r[i]+c[j])%2==1:
                    ans+=1
        return ans
