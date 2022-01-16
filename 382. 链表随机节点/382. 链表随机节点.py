# Definition for singly-linked list.
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
    def getRandom(self) -> int:
        ans = 0
        p = self.head
        n = 0
        while p:
            n=n+1
            rand = random.randint(1,n) #抽取到新数据的概率是1/N
            if(rand == n):             #当抽取到新数据的时候，保留新数据，否则保留原数据
                ans = p.val
            p = p.next
        return ans        



