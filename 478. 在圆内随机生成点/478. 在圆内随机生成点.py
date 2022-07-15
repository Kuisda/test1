from typing import List
import random
import math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center
    def randPoint(self) -> List[float]:
        u,theta = random.random(),random.random()*2*math.pi#random.random()生成0-1之间的随机数
        r = math.sqrt(u)#二维空间中取到距离为r的圆环的概率不是等概率的，例如取到小于r/2的概率是1/4，为了保证等概率可以在r^2中取随机数
        return [self.x + r*math.cos(theta)*self.radius,self.y+r*math.sin(theta)*self.radius]