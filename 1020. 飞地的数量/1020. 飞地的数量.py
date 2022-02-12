from typing import List
from queue import Queue
from collections import defaultdict

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = Queue()
        dic = defaultdict(int)
        #boolean[][] visited 还是使用visit矩阵比较好
        Tnum = 0
        Cnum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    Tnum+=1
                    dic[(i,j)]=0
                    if i==0 or i==m-1 or j==0 or j==n-1:
                        q.put((i,j))
                        dic[(i,j)]=1
                        Cnum+=1
        while not q.empty():
            posx,posy = q.get()

            for x,y in ((posx-1,posy),(posx+1,posy),(posx,posy-1),(posx,posy+1)):
                if 0<=x<m and 0<=y<n and grid[x][y]==1 and dic[(x,y)]==0:
                    dic[(x,y)]=1
                    Cnum+=1
                    q.put((x,y))
        return  Tnum-Cnum

x = Solution()
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
ans = x.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])