from typing import List
from sortedcontainers import SortedList
from collections import defaultdict
#首先把按员工名的时间list摘出来，排序然后判断相邻三个以内是否存在时间差小于1h
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def JudgeTime(s1:str,s2:str)->bool:
            return abs(int(s1[0:2])*60+int(s1[3:5])-int(s2[0:2])*60-int(s2[3:5]))<=60
        slist = SortedList()
        d = defaultdict()
        for name,time in zip(keyName,keyTime):
            if name not in d:
                d[name] = [time]
            else:
                d[name].append(time)
        for name,times in d.items():
            times.sort()
            if any(JudgeTime(s1,s2) for s1,s2 in zip(times,times[2:])):
                slist.add(name)
        return list(slist)

        

x = Solution()
x.alertNames(["a","a","a","a","a","b","b","b","b","b","b"],
["23:20","11:09","23:30","23:02","15:28","22:57","23:40","03:43","21:55","20:38","00:19"])

        