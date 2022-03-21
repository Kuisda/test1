from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#深度优先+set

class Solution:
    def __init__(self):
        self.s =set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k-root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left,k) or self.findTarget(root.right,k)        
