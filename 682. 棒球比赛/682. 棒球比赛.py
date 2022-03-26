from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        sum=0
        clist = []
        for ch in ops:
            if ch=='C':
                sum-=clist[-1]
                del clist[-1]
            elif ch=='D':
                clist.append(clist[-1]*2)
                sum+=clist[-1]
            elif ch=='+':
                clist.append(clist[-2]+clist[-1])
                sum+=clist[-1]
            else:
                clist.append(int(ch))
                sum+=clist[-1]
        return sum        