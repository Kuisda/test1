#有序列表(有序集合)存储当前可用服务器的id,按照id升序排列
#堆保证队首的服务器的处理结束时间最小
#独立维护每一个处理器的状态，当处理器处于busy时需要记录其id以及处理结束的时刻，处于available时则只需要记录id
from heapq import heappop
from typing import List
from sortedcontainers import SortedList
from heapq import heappush

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy=[]
        requests = [0]*k
        for i,(start,t) in enumerate(zip(arrival,load)):
            while busy and busy[0][0] <=start:
                available.add(busy[0][1])
                heappop(busy)
            if len(available) ==0:
                continue
            j = available.bisect_left(i%k)
            if j==len(available): #查找失败，选用编号最小的处理器
                j=0
            id = available[j]
            requests[id]+=1
            heappush(busy,(start+t,id))
            available.remove(id)
        maxRequest = max(requests)

        return [i for i,req in enumerate(requests) if req == maxRequest]        

                
