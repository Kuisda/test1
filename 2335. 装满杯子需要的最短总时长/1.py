from typing import List
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        return amount[2] if amount[2]>amount[0]+amount[1] else (sum(amount)+1)//2
