from typing import List

def changeToMinute(str) -> int:
    hour = (ord(str[0])-ord('0'))*10+(ord(str[1])-ord('0'))
    minute = (ord(str[3])-ord('0'))*10+(ord(str[4])-ord('0'))
    return hour*60+minute


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if(len(timePoints)>1440): #抽屉原理，各个位置总计有24*60 = 1440种可能，数量超过则必定有相同
            return 0
        list = [changeToMinute(x) for x in timePoints]
        list.sort()
        min = 2000
        for i in range(len(list)-1):
            if(list[i+1]-list[i]<min):
                min = list[i+1]-list[i]
                print(min)
        last = 1440-list[-1]+list[0]
        if(last<min):
            min = last

        return min
"""
x = Solution()
timePoints = ["00:00","23:59","00:00"]
num = x.findMinDifference(timePoints)  
print(num)
"""