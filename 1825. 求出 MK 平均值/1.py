from collections import deque
from sortedcontainers import SortedList
class MKAverage:
    def __init__(self, m: int, k: int):
        self.m=m
        self.k=k
        self.midSum = 0
        self.low = SortedList()#最小的k个
        self.mid = SortedList()#剩下的
        self.high= SortedList()#最大的k个
        self.d = deque()
    def addElement(self, num: int) -> None:
        if not self.low or num<self.low[-1]:#如果在low为空或者当前num小于low数组的最大值，则num处于最小的k个之中
            self.low.add(num)
        elif not self.high or num>self.high[0]:
            self.high.add(num)
        else:#否则放到中间
            self.mid.add(num)
            self.midSum+=num
        self.d.append(num)#在队列上加入
        if len(self.d) > self.m:#判断队列是否超过了m，如果是则需要pop掉队首，然后在sortedList中也将其删掉
            x = self.d.popleft()
            if x in self.low:
                self.low.remove(x)
            elif x in self.high:
                self.high.remove(x)
            else:
                self.mid.remove(x)
                self.midSum-=x
        
        #然后，还需要判断mid和high是否出现大于k的情况，如果len(mid)>k,要移动多出的部分到mid中，对high的处理也相似
        while len(self.low)>self.k:
            x = self.low.pop()
            self.mid.add(x)
            self.midSum+=x
        while len(self.high)>self.k:
            x = self.high.pop(0)
            self.mid.add(x)
            self.midSum+=x
        #最后还要判断low和high是否出现小于k的情况，这个情况是由于队列中元素的变化而产生，根据情况要把mid中的元素移过去补齐
        while len(self.low)<self.k and self.mid:
            x = self.mid.pop(0)
            self.low.add(x)
            self.midSum-=x
        while len(self.high)<self.k and self.mid:
            x = self.mid.pop()
            self.high.add(x)
            self.midSum-=x
            
    def calculateMKAverage(self) -> int:
        return -1 if len(self.d)<self.m else self.midSum // len(self.mid)