from typing import List
from collections import defaultdict
from math import gcd
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(2,n+1):
            for j in range(1,i):
                if gcd(i,j)==1:
                    ans.append('{}/{}'.format(j,i))
        return ans 

x = Solution()
ans = x.simplifiedFractions(4)           
print(ans)