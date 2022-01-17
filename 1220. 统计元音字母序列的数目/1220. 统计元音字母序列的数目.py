#只需要到n-1次迭代就可以进入到n状态
#动态规划
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = (1,1,1,1,1)

        for _ in range(n-1):
            dp = ((dp[1]+dp[2]+dp[4])%1000000007,(dp[0]+dp[2])%1000000007,(dp[1]+dp[3])%1000000007,dp[2]%1000000007,(dp[2]+dp[3])%1000000007)

        return sum(dp)%1000000007