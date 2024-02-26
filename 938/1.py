from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ll = []
        def inorder(root:Optional[TreeNode]):
            if root:
                inorder(root.left)
                ll.append(root.val)
                inorder(root.right)
        inorder(root)
        sum = 0
        for v in ll:
            if v>=low and v<=high:
                sum+=v
        return sum