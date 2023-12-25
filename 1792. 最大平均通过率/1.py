from heapq import heapify
from heapq import heapreplace
from typing import List

class Entry:
    __slots__ = 'p','t'#限制实例进行变量声明
    def __init__(self, p: int, t: int):
        self.p = p
        self.t = t
    def __lt__(self, b:'Entry'):#这里的逻辑是：堆会是小顶堆，使用heapify进行比较时会按照Entry的__lt__方法进行比较，__lt__返回为true->self小于b->self更可能为堆顶
        #迁移到self对b有更高的优先级对应的表达式为(self.t+1)*self.t*(b.t-b.p)<(b.t+1)*b.t*(self.t-self.p)，也就是要这个表达式在__lt__中返回true
        return (self.t+1)*self.t*(b.t-b.p)<(b.t+1)*b.t*(self.t-self.p)
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes]
        heapify(h)#转换为堆
        for _ in range(extraStudents):
            heapreplace(h,Entry(h[0].p+1,h[0].t+1))#pop到堆顶，替换然后返回
        return sum(e.p/e.t for e in h)/len(h)   

            
        