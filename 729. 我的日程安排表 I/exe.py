"""
class MyCalendar:
    def __init__(self):
        self.cal = []
    def book(self, start: int, end: int) -> bool:
        if len(self.cal)==0:
            self.cal.append([start,end])
            return True
        for i,section in enumerate(self.cal):
            l,r = section[0],section[1]
            if not (start>=r or end<=l):
                return False
        self.cal.append([start,end])
        return True
"""
#通过二分查找，首先二分查找到下界高于end的时间段，然后查看这个时间段的前一个时间段的结束时间是否早于start
# SortedDict保证了key的顺序以及可比较性，其自带的bisect方法是根据key序列进行二分查找的
#如果end小于任何一个时间段的起始时间(返回index==0)，则必然可以满足不会产生时间段重叠
from sortedcontainers import SortedDict
class MyCalendar:
    def __init__(self):
        self.cal = SortedDict()
    def book(self, start: int, end: int) -> bool:
        index = self.cal.bisect_left(end)
        if index == 0 or self.cal.items()[index-1][1]<=start:
            self.cal[start] = end
            return True
        return False

x = MyCalendar()
x.book(10,20)
x.book(15,25)
x.book(20,30)