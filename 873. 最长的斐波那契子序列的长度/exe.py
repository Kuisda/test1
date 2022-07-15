#状态定义：dp[i][j]表示以arr[i],arr[j]结尾的斐波那契序列(....,arr[i],arr[j])的最大长度
#状态转移：如果arr[i],arr[j]序列的前一位必定满足arr[j]-arr[i] = arr[k], dp[i][j] = max(dp[k][i]+1),其中k下标应该在i下标的左边
from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0]*n for _ in range(n)]
        dic = {x:i for i,x in enumerate(arr)}#用于记录每一个值对应的下标
        ans = 0

        for i in range(n):
            for j in range(i+1,n):
                dp[i][j] = 2
        
        for i in range(n):
            for j in range(i+1,n):
                diff = arr[j]-arr[i]
                if diff in dic:
                    k = dic[diff]
                    if k<i:
                        dp[i][j] = max(dp[i][j],dp[k][i]+1)
                ans = max(ans,dp[i][j])
        
        return ans if ans>2 else 0
        

