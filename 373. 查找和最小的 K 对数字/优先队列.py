import math
import heapq
from queue import PriorityQueue
from typing import List

#超时的主要原因是对所有元素进行排序了，实际上不用把所有元素都排序
#最小值一定是[1,1]位置的两个，第二,三小值则在[1,2],[2,1]中选择，第四五六则在[1,3],[2,2],[3,1]中选择，所以选择大概一个左上三角的位置(k*k)就可以得到前k个值
#每次一行入队列:第一次[1,1],...,[1,k]第二次[2,1],...,[2,k-1]每次入的行都是升序的，不需要排序，减少了队列内排序时间


def takesecond(elem):
    return elem[1]


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
#默认的是升序
        pq = PriorityQueue()
        ans  = []
        z=1
        for i in range(n1):
            for j  in range(n2):
                pq.put((nums1[i]+nums2[j],z))
                z+=1

        if(k>z-1):
            k=z-1 #z最后又加了一次
        for i in range(k):
            tuple = pq.get()
            serial = float(tuple[1])
            t1 = math.ceil( serial/n2 )
            t2 = int(serial)-(t1-1)*n2
            ans.append([nums1[t1-1],nums2[t2-1]])

        return ans

    def optimize(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        pq = PriorityQueue()
        ans = []
        for j in range(min(k,n2)):
            pq.put((nums1[0]+nums2[j],0,j))
        while pq and len(ans)<min(k,n1*n2):
            _,i,j = pq.get()
            ans.append([nums1[i],nums2[j]])
            if(i+1<n1):
                pq.put((nums1[i+1]+nums2[j],i+1,j))
        return ans        

""" 使用最小堆来做
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
"""