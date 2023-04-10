# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



#从后往前看就是一个单调栈的问题
#首先翻转链表然后顺序的按照单调栈问题来处理即可
# 维持一个从底到顶递减的栈
# 如果当前节点val比栈顶大，那么栈顶出栈直到栈顶比cur.val大为止
class Solution:
    def reverseList(self,head:Optional[ListNode])->Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        head = self.reverseList(head)
        stack = [head.val]
        ans = [0]
        cur = head.next
        while cur:
            if cur.val <stack[-1]:
                ans.append(stack[-1])
            else:
                while stack and stack[-1]<=cur.val:
                    stack.pop()
                if stack:#stack 非空，说明cur.val <stack[-1]
                    ans.append(stack[-1])
                else:#stack 为空
                    ans.append(0)
            stack.append(cur.val)
            cur = cur.next
        return ans[::-1]
    





            
             


