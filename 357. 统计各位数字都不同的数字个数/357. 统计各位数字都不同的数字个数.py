#排列组合
#n为1时全部符合要求，n>1时第一位有9种可能，第二位到最后一位则有9,8，...9-（位数-1）种可能
#n=2，对应的符合要求的是9*9+10(n=1时满足的数量)
#n=3, 对应符合要求的是9*8*7+9*9+10
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 10
        res,cur = 10,9
        for i in range(n-1):
            cur*=9-i
            res+=cur
        return sum


        

