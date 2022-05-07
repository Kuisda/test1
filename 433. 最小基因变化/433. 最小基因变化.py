#bank的作用在于从start开始的每一次变换结果都必须在bank中
#bfs 每一次遍历所有可能的变化，并把符合bank的变化加入到队列中
from collections import deque
from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        if end not in bank:
            return -1
        q = deque([(start,0)])
        bank = set(bank)
        while q:
            cur,step = q.popleft()
            for i,x in enumerate(start):
                for y in "ACGT":
                    s = cur[:i]+y+cur[i+1:]
                    if s in bank:
                        if s == end:
                            return step+1
                        bank.remove(s)
                        q.append((s,step+1))
        return -1

