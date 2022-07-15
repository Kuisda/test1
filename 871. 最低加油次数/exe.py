from typing import List
import heapq
#next step就是下一个station或者终点target
#所有途径的station的加油量都加入到大顶堆中，堆顶就是最大的加油量
#计算从prev step到现在这个step的耗油量，如果大于当前的耗油量则在堆中选择已过加油站中最大加油量的进行加油，加油次数加一
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n =len(stations)
        current,prev,c_fuel=0,0,startFuel
        heap = []
        ans = 0
        for i in range(n+1):
            current = stations[i][0] if i<n else target
            c_fuel -= current-prev
            while c_fuel<0 and heap:
                c_fuel += -heapq.heappop(heap)
                ans+=1
            if c_fuel<0:
                return -1
            if i<n:
                heapq.heappush(heap,-stations[i][1])
                prev = current
        return ans







            
        