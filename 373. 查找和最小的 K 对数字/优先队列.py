import math
import heapq
from queue import PriorityQueue
from typing import List


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

def test(nums1: List[int], nums2: List[int], k: int):
        n1 = len(nums1)
        n2 = len(nums2)

        list = []
        z=0
        for i in range(n1):
            for j  in range(n2):
                temp = [z,nums1[i]+nums2[j]]
                list.append(temp)
                z+=1
        list.sort(key= takesecond)
        print(z)
        if(z<k):
            k=z
        print(k)    


nums1 = [1,2]
nums2 = [3]
k = 3 
test(nums1,nums2,k = 3) 