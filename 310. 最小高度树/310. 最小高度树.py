#设两个节点的最长距离为mardist，最小高度树高度为ceil(mardist/2),且根节点在最长距离两端叶节点x，y之间的路径上
# (如果不在路径上，则根节点需要首先到达路径上的一个节点，然后再到x，y节点处，这个路径一定大于ceil(mardist/2)的)

#根节点实际上应该在x，y路径上中间的位置
#假设最长路径结点为p1,p2...pm,最长路径长度为m-1,
#   如果 m 为偶数，此时最小高度树的根节点为m/2或m/2+1,最小高度树的最大高度为m/2
#   如果 m 为奇数，根节点为（m+1）/2，最小高度树的最大高度为（m-1）/2

#寻找最长路径：选取任意节点p，dfs/bfs找到距离p最长的路径终点x，找距离x最长路径的终点y，dist[x][y]即为所求

from typing import List
from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        #将边信息转换为节点连接信息，能够通过节点下标访问连接到的边    
        g = [[]for _ in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0]*n

        def bfs(start:int):
            vis = [False]*n
            vis[start] = True
            q = deque([start])
            while(q):
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x#储存路径，在一次bfs中不会出现重复覆盖的情况，因为子节点不会有两个父结点
                        q.append(y)
            return x #最后一个入队列的一定是距离初始结点start最远的

        x = bfs(0) #与结点0最远的结点x
        y = bfs(x) #与结点x最远的结点y，注意这里的执行顺序下parents储存的是以x为根节点的树

        path=[]
        parents[x] =-1
        while y!=-1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m//2]] if m%2 else [path[m//2-1],path[m//2]]


                    
           
