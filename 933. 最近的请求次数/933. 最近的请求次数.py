#用滑动窗口也可以，记录一个左指针指向大于t-3000的第一个位置
from collections import deque
class RecentCounter:
    def __init__(self):
        self.q = deque()
    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0]<t-3000:
           self.q.popleft()
        return len(self.q)