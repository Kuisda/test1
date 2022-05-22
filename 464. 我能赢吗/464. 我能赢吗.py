from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache #记忆化，好像会将一部分结果储存在cache中以减少运算时间
        def dfs(usedNumber:int,currentTotal:int)->bool:
            for i in range(maxChoosableInteger):
                if(usedNumber>>i) &1 ==0: #以i位置的0表示数字i没有被选用
                    #i+1是因为i从0开始
                    if currentTotal+i+1 >= desiredTotal or not dfs(usedNumber|(1<<i),currentTotal+i+1):
                        #后部分表示选择数字i使得对方无法获胜
                        return True
            return False
        #若可选数总和都不超过目标则直接判断为False
        return (1+maxChoosableInteger)*maxChoosableInteger//2>=desiredTotal and dfs(0,0)