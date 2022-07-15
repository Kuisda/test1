from typing import List
#动态规划 dp[i][j]表示从0到i号的房子且i号的房子使用j颜色染色时花费的最小成本
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp =[[0]*3 for i in range(n)]#dp = [[0]*3]*len(costs)这样的是浅复制，一列的所有行都是关联的
        for j in range(3):
            dp[0][j] = costs[0][j]
        for i in range(1,len(costs)):
            dp[i][0] = min(dp[i-1][1],dp[i-1][2])+costs[i][0]
            dp[i][1] = min(dp[i-1][0],dp[i-1][2])+costs[i][1]
            dp[i][2] = min(dp[i-1][0],dp[i-1][1])+costs[i][2]
        return min(dp[n-1])
"""
#其实可以直接在原列表中dp
#这样省去了对[0][0],[0][1],[0][2]的初始化以及额外空间的创建
for i in range(1,len(costs)):
            costs[i][0] = min(costs[i-1][1],costs[i-1][2])+costs[i][0]
            costs[i][1] = min(costs[i-1][0],costs[i-1][2])+costs[i][1]
            costs[i][2] = min(costs[i-1][0],costs[i-1][1])+costs[i][2]
"""



x = Solution()
minans = x.minCost([[17,2,17],[16,16,5],[14,3,19]])