from collections import defaultdict
#以起点和长度为基础做动态规划，确定起点后每有下一项符合的，则以该字符为起点的字符串的适合的子串数量+1
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i,ch in enumerate(p):
            if i>0 and (ord(ch)-ord(p[i-1])) % 26==1: #ascii码前后之差为1或者-25
                k+=1
            else:
                k = 1
            dp[ch] = max(dp[ch],k)
        return sum(dp.values())
x = Solution()
x.findSubstringInWraproundString("zab")