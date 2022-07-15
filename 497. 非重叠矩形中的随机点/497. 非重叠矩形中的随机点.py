from bisect import bisect_right
from typing import List
from random import randrange

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.point = [0]
        for a,b,x,y in rects:
            self.point.append(self.sum[-1]+(x-a+1)*(y-b+1))#按顺序记录每个矩形还有多少点，按照前缀和的形式储存：[0,1]->(下一个矩形有5个点)[0,1,6]

 
    def pick(self) -> List[int]:
        k = randrange(self.point[-1])#randrange([start],stop,[step])1,3号元素可省，在[stop,start)按照step取随机数
        rectIndex = bisect_right(self.point,k)-1
        a,b,_,y = self.rects[rectIndex]
        da,db = divmod(k-self.point[rectIndex],y-b+1)
        return [a+da,b+db]


