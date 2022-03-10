import queue
from typing import List
from queue import Queue
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def dfs(node:'Node'):
            if node is None:
                return
            ans.append(node.val)
            for ch in node.children:
                dfs(ch)

        dfs(root)

        return ans            



