from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#由于是逆序排列，可以直接对应位相加，对10求模就可以得到该位的值以及进位。
#还是推荐创造一个新链表，在原链表上改动会出现很多问题，例如l1，l2的长度不一致时你要选择哪一个，要怎么处理长短链表的相加等问题

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cb = 0
        p1,p2 = l1,l2
        head = ListNode()
        node = head
        while p1!=None and p2!=None:
            sum = p1.val+p2.val+cb
            cb = int(sum/10)
            vval = sum%10
            newnode = ListNode(val=vval)
            node.next = newnode
            node = node.next
            p1 = p1.next
            p2 = p2.next
        while p1!=None:
            sum = p1.val+cb
            cb = int(sum/10)
            vval = sum%10
            newnode = ListNode(val=vval)
            node.next = newnode
            node = node.next
            p1 = p1.next
        while p2!=None:
            sum = p2.val+cb
            cb = int(sum/10)
            vval = sum%10
            newnode = ListNode(val=vval)
            node.next = newnode
            node = node.next
            p2 = p2.next
        if cb!=0:
            newnode = ListNode(val=cb)
            node.next = newnode
            node = node.next

        return head.next
        
            