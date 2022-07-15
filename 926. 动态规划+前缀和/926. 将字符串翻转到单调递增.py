#前缀和+动态规划
#一个简单的二分思路，按照位置j来二分，前面的要全部置换成0，后面的要全部置换为1
#根据前缀和能够知道两个划分区间包含的0,1数目
#注意这里的前缀和p[i]表示的是[0,i-1]，所以遍历到[0,n-1]的前缀和需要访问p[n]
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        pre_sum = [0]
        n = len(s)
        for ch in s:
            pre_sum.append(pre_sum[-1]+int(ch))
        
        return min(pre_sum[j]+(n-j)-(pre_sum[-1]-pre_sum[j]) for j in range(n+1))


x = Solution()
x.minFlipsMonoIncr("00011000")