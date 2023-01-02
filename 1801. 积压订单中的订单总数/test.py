import heapq
#s[0]就是小顶堆的堆顶
s = []
heapq.heappush(s,7)
heapq.heappush(s,5)
heapq.heappush(s,4)
print(s[0])
heapq.heappop(s)
print(s[0])