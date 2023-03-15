#以节点为单位找统计每个节点的边数，找到两个节点，在假设这两个节点有公共边则只算一次的情况下，使得两个节点的变数和最大
#注意公共边实际上只可能出现一条，因为两个节点之间只有一条路径
from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=[[False for _ in range(n)] for _ in range(n)]
        degree = [0 for _ in range(n)]
        for road in roads:
            x,y= road[0],road[1]
            degree[x]+=1
            degree[y]+=1
            graph[x][y]=True
            graph[y][x]=True
        
        #最大degree列表和次大degree列表
        firstArr,secondArr = [],[]
        max,secondmax = -1,-2
        for i in range(n):
            if degree[i]>max:
                secondArr = firstArr
                secondmax = max
                firstArr = [i]
                max = degree[i]
            elif degree[i]==max:
                firstArr.append(i)
            elif degree[i]>secondmax:
                secondArr = [i]
                secondmax = degree[i]
            elif degree[i]==secondmax:
                secondArr.append(i)
        #firstArr至少长度为1，如果为1则另一个节点在次大列表secondArr中找，然后还需要判断一下次大列表中是否存在没有公共边的节点   
        if len(firstArr)==1:
            num = firstArr[0]
            for u in secondArr:
                if not graph[num][u]:
                    return max+secondmax
            return max+secondmax-1
        #firstArr长度大于1的时候两个节点都在firstArr中找到
        if len(firstArr)>=2:
            for u in firstArr:
                for v in firstArr:
                    if u!=v and not graph[u][v]:
                        return max * 2
            return max * 2 -1



x = Solution()
x.maximalNetworkRank(8,[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])
            
        
        
