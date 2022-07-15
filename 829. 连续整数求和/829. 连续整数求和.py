#k个连续整数最小值为(1+k)*k/2 n>=(1+k)*k/2 => k(k+1)<2n这是枚举的范围
# 最小整数x开始，假设连续的k个整数，即为[x,x+k-1]，然后使用平方和，对结果计算出x，查看x为整数的条件，记得要分奇偶
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        def isKConsecutive(n:int,k:int)->bool:
            if k%2:
                return n%k==0
            return n%k and (2*n)%k==0
        ans = 0
        k = 1
        while k*(k+1) <=n*2:
            if isKConsecutive(n,k):
                ans+=1
            k+=1
        return ans
