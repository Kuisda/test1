#https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make/solution/by-yyycz-88ij/
from typing import List
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        r=1
        for coin in coins:
            if coin > r: break
            r += coin
        return r