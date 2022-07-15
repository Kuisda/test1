from typing import List
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        r = [0]*m
        c = [0]*n
        ans=0
        for x,y in indices:
            r[x]+=1
            c[y]+=1
        oddx = sum(row%2 for row in r)
        oddy = sum(col%2 for col in c)
#行计数为奇数，列计数为偶数，那么这个位置[r,c]才是奇数
#row中值为奇数的数量为oddx，col中值为奇数的数量为oddy
#如果row[x]为奇数，那么只有列计数为偶数的列对应位置是奇数 对应所有row为奇数的行，有oddx*(n-oddy)个位置为奇数
#同理row[y]为偶数，那么只有列计数为奇数的列对应位置是奇数，有(m-oddx)*oddy
        return oddx*(n-oddy)+(m-oddx)*oddy