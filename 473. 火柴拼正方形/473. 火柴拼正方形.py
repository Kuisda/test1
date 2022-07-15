#回溯法
from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ssum = sum(matchsticks)
        if ssum%4 !=0:
            return False
        matchsticks.sort(reverse=True)
        num = ssum//4

        edges = [0]*4
        def dfs(idx:int)->bool:
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] +=matchsticks[idx]
                if edges[i] <= num and dfs(idx+1):
                    return True
                edges[i] -= matchsticks[idx]
            return False
        return dfs(0)


x = Solution()
x.makesquare([5,5,5,5,4,4,4,4,3,3,3,3])

            
