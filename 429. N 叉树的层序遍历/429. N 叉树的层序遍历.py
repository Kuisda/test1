from typing import List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
#cnt保留了一层的所有结点在q中的数量，每次把一层的结点值全部放在一个暂时的列表中，并把一层结点的所有子节点都添加到queue中
#最后把暂存的列表添加到ans中
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque([(root)])
        ans = []
        while(q):
            cnt = len(q)
            templist = []
            for _ in range(cnt):
                x = q.popleft()
                templist.append(x.val)
                for child in x.children: 
                    q.append(child)
            ans.append(templist)
        return ans            

