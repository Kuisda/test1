from typing import List
from collections import defaultdict
from collections import Counter

class DetectSquares:

    def __init__(self):
        self.xhash = defaultdict(list)
        self.yhash = defaultdict(list)

    def add(self, point: List[int]) -> None:
        self.xhash[point[0]].append(point[1])
        self.yhash[point[1]].append(point[0])
        return


    def count(self, point: List[int]) -> int:
        count = 0
        for y in self.xhash[point[0]]:
            if y!=point[1]: 
                len = y-point[1]  
#查找到同x的另一个y后就可以确定正方形的边长，根据边长可以确定第三个点x的两种可能取值，分别在hash中查找这两种出现的情况
                x1 = point[0]+len
                x1time = self.yhash[point[1]].count(x1)
                if x1time>0:
                    temp = self.xhash[x1].count(y)
                    count+=x1time*temp

                x2 = point[0]-len
                x2time = self.yhash[point[1]].count(x2)
                if x2time>0:
                    temp = self.xhash[x2].count(y)
                    count+=x2time*temp
        return count
#哈希表+counter计数器结构
class Solution2:
    def __init__(self):
        self.map = defaultdict(Counter)
    def add(self, point: List[int]) -> None:
        x,y = point
        self.map[y][x] +=1
    def count(self, point: List[int]) -> int: 
        count =0
        x,y = point

        if not y in self.map:
            return 0
        yCnt = self.map[y]

        for col,colCnt in self.map.items(): #items()以列表的形式返回键值对
            if col !=y:
                d = col - y
                count +=colCnt[x] * yCnt[x+d] * colCnt[x+d]
                count +=colCnt[x] * yCnt[x-d] * colCnt[x-d]
        return count



"""
c = DetectSquares()
c.add([8,8])
c.add([8,0])
c.add([8,0])
c.add([0,0])
print(c.xhash)
print(c.yhash)
print(c.count([0,8]))
"""