from typing import List
from collections import Counter
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        #利用set去除重复元素
        light_set = set()
        row,col,diagonal,antiDiagonal = Counter(),Counter(),Counter(),Counter()
        #row,col记录照亮的行和列
        #用正对角线y=x+k 与x轴的交点表示正对角线的位置：对点(a,b)，交点x = b-a
        #同理用负对角线y=-x+k与y轴的交点表示负对角线的位置，对点(a,b),交点y = a+b 
        for (r,c) in lamps:
            if (r,c) in light_set:
                continue
            light_set.add((r,c))
            row[r]+=1
            col[c]+=1
            diagonal[r-c]+=1 #按照坐标轴的规则(a,b)a表示列b表示行
            antiDiagonal[r+c]+=1
        ans = [0]*len(queries)
        for i,(r,c) in enumerate(queries):
            if row[r] or col[c] or diagonal[r-c] or antiDiagonal[r+c]:
                ans[i]=1
            for x in range(c-1,c+2): #左闭右开    
                for y in range(r-1,r+2):
                    if x<0 or x>=n or y<0 or y>=n or (y,x) not in light_set:
                        continue
                    light_set.remove((y,x))
                    row[y]-=1
                    col[x]-=1
                    diagonal[y-x]-=1
                    antiDiagonal[y+x]-=1
        return ans