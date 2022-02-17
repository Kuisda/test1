class Solution:
    #反向的求任意终点到起始点(row,column)的概率，与计算起始点到任意点的概率和是等价的
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0]*n for _ in range(n)]for _ in range(k+1)]

        for step in range(k+1):
            for i in range(n):
                for j in range(n):
                    if step==0:
                        dp[step][i][j] = 1
                    else:
                        for di,dj in ((-2,-1),(-2,1),(2,-1),(2,1),(1,-2),(-1,-2),(-1,2),(1,2)):
                            ni,nj = i+di,j+dj
                            if 0<=ni <n and 0<=nj<n:
                                dp[step][i][j] +=dp[step-1][ni][nj]/8
                                #step步跳到点(i,j)的概率是step-1步中能跳到点(i,j)位置的所有点的概率*1/8的和
        return dp[k][row][column]                        