from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def PostOrder(node:Node):
            if(node):
                for ch in node.children:
                    PostOrder(ch)
                ans.append(node.val)
        PostOrder(root)

        return ans        
