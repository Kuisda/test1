from collections import deque
from collections import defaultdict
from typing import List
#直接根据次最短路径来判断次最短时间，但是有没有可能由于等待时间第三短路径的等待时间比次短路径的等待时间少很多
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        #visitList = [[False for i in range(n+1)] for i in range(n+1)]
        #FirstNodeTime = [float("inf") for i in n+1] #[0,n]
        #FirstNodeTime[1] = 0
        #SecondNodeTime = [float("inf") for i in n+1]
        #SecondNodeTime[1] = 0

        NodeEdgeDict = defaultdict(list)
        for u,v in edges:
            NodeEdgeDict[u].append(v)
            NodeEdgeDict[v].append(u)

        dist = [[float("inf")] *2 for i in range(n+1)]#表示最短路径以及次短路径
        dist[1][0] = 0

        q = deque()#[结点，到该节点的访问时间]
        q.append([1,0])

        while q:
            num = q.popleft()
            for i in NodeEdgeDict[num[0]]:
                d = num[1]+1
                #当前路径长d比之前记录的最短路径短：原最短路径替换次短路径，d替换原最短路径
                if d <dist[i][0]:
                    dist[i][1] = dist[i][0]
                    dist[i][0] = d
                    q.append([i,d])
                elif d>dist[i][0] and d<dist[i][1]:
                    dist[i][1] = d
                    q.append([i,d])
        ans = 0
        for _ in range(dist[n][1]):
            if ans %(change*2) >=change:
                ans+=change*2-ans%(change*2)
            ans+=time
        return ans


