class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag=2
        while n!=0:
            if flag==n&1:
                return False
            else:
                flag=n&1
                n = n>>1
        return True

x = Solution()
x.hasAlternatingBits(5)

class Solution:
    def hasAlternatingBits_1(self, n: int) -> bool:
        a = n^(n>>1)
        return a & (a+1) ==0 #判断是否a的全部位都为1