from typing import List
from collections import deque
#注意：虽然砍树要求按数字从低到高砍，但是所有带数字的格子都是可以走的
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def BFS(sx:int,sy:int,tx:int,ty:int):#广度优先搜索第一个搜索到目标(tx,ty)时一定是最短的到达路径
            m,n = len(forest),len(forest[0])
            q = deque([(0,sx,sy)])
            vis = {(sx,sy)}
            while q:
                d,x,y = q.popleft()
                if x ==tx and y==ty:
                    return d
                for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0<=nx<m and 0<=ny<n and forest[nx][ny] and (nx,ny) not in vis:
                        vis.add((nx,ny))
                        q.append((d+1,nx,ny))
            return -1
        trees = sorted((h,i,j) for i,row in enumerate(forest) for j,h in enumerate(row) if h>1)
        #[(2,x,y),(3,x,y),...,]
        ans = 0
        preI,preJ = 0,0
        #当前位置的数字是i，每次寻找到达i+1的最短路径
        for _,i,j in trees:
            d = BFS(preI,preJ,i,j)
            if d<0:
                return -1
            ans +=d
            preI,preJ = i,j
        return ans

