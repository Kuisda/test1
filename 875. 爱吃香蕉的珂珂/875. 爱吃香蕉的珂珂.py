from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)
        L, R = 1, piles[-1]
        while L <= R:
            M = L + ((R - L) >> 1)
            need = sum([ceil(x / M) for x in piles])
            if need > h:
                L = M + 1
            else:
                R = M - 1
        return L