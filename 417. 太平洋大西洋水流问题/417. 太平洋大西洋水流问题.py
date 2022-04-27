#图一般使用广度优先或者深度优先
#从太平洋(上，左边界)以及大西洋(右下边界)对应边界开始进行广度或者深度优先搜索，找比当前点更高的周围点
#如果一个点同时存在于 从太平洋边界处得到的搜索结果 以及从大西洋边界处开始得到的搜索结果，那么这个点可以同时抵达两边，也就是所求
from typing import List
from typing import Tuple
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])

        def bfs(starts:List[Tuple[int, int]])->set():
            q = deque(starts)
            visited = set(starts)
            while q:
                x,y = q.popleft()
                for nx,ny in ((x,y+1),(x,y-1),(x-1,y),(x+1,y)):
                    if 0<=nx <m and 0<=ny<n and heights[nx][ny]>=heights[x][y] and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))
            return visited
        
        pacific = [(0,i) for i in range(n)]+[(i,0) for i in range(1,m)]#加入太平洋相连的上，左边界
        atlantic = [(m-1,i) for i in range(n)]+[(i,n-1) for i in range(m-1)]#这里下右边界重合的点是(m-1，n-1)

        return list(bfs(pacific)&bfs(atlantic))

