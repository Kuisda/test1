from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        pairs = sorted(zip(aliceValues,bobValues),key=lambda p:-(p[0] + p[1]))
        alice ,bob = 0,0
        flag = 1
        for pair in pairs:
            if flag == 1:
                alice += pair[0]
                flag =0
            else:
                bob +=pair[1]
                flag = 1
        if alice == bob:
            return 0
        return 1 if alice > bob else -1
    

c = Solution()
c.stoneGameVI([1,2],[3,1])