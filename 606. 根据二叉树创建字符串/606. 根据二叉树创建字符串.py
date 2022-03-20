#当只存在右子树的时候左子树的位置要加一对括号，只存在左子树时不需要为右子树的位置加上一对括号。
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = ""
        def preOrder(node:TreeNode):
            nonlocal s
            s +=str(node.val)    
            if node.left:
                s+='('
                preOrder(node.left)
                s+=')'
            elif not node.left and node.right:
                s+='()'
            
            if node.right:    
                s+='('
                preOrder(node.right)
                s+=')'

        preOrder(root)
        return s    
