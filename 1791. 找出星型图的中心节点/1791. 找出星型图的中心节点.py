from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u_set = set()
        for i,j in edges:
            if i in u_set:
                return i
            elif j in u_set:
                return j
            u_set.add(i)
            u_set.add(j)            