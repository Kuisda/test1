# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prea = list1
        for _ in range(a-1):#达到a的前一位，不用思考从0开始的这个问题，因为a是下标也是从0开始的，所以就按照个数来理解就行，要到prea就是a-1
            prea = prea.next
        preb = prea
        for _ in range(b-a+2):
            preb = preb.next
        prea.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = preb
        return list1

