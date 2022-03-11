from re import S
from typing import List
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]

        for i,p in enumerate(parents):#子节点列表
            if p!=-1:
                children[p].append(i)

        maxScore,count = 0,0
        def dfs(node:int) -> int: #从根节点0开始，会递归的统计所有结点的删除后score值，然后取最大的即可
            score = 1
            size = n-1
            for i in children(node):
                s = dfs(i)
                score *=s
                size -=S
            if size!=0: #被node分割的父结点
                score*=size
            nonlocal maxScore,count
            if score==maxScore:
                count+=1
            elif score>maxScore:
                maxScore = score
                count = 1
            return count 
        dfs(0)

        return count



                


