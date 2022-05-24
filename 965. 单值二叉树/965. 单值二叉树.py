from asyncio.windows_events import NULL


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def preorder(node:TreeNode,num:int)->bool:
            if node is None:
                return True
            if node.val!=num:
                return False
            if preorder(node.left,num)==False:
                return False
            if preorder(node.right,num)==False:
                return False
            return True

        return preorder(root,root.val)


