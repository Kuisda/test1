from math import floor 
from math import ceil

class Solution:
    def numberOfMatches(self, n: int) -> int:
        #return n-1 
        ans = 0
        while(n!=1):
            ans += floor(n/2)
            n = ceil(n/2)

        return ans