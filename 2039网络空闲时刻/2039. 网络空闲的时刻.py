from collections import deque
from typing import List
from collections import deque

#广度优先搜索，从主服务器结点开始，先搜索到的点对应的路径，就是该点到主服务器结点的最短路径
#找到最短路径后可以直接根据patience[i]计算出最后一次发送信息的时间，进而算出结点进入空闲的时间
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        g = [[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = [False] *n
        vis[0] = True
        q = deque([0])
        ans,dist = 0,1
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if vis[v]:
                        continue    
                    vis[v] = True
                    q.append(v)
                    ans = max(ans,(dist*2-1)//patience[v]*patience[v]+dist*2+1)
            dist+=1
        return ans            