from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dict = {}
        for i in range(len(inorder)):
            dict[inorder[i]] = i 
        def f(in_left:int,in_right:int)-> Optional[TreeNode]:
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)

            index = dict[val]

            root.right = f(index+1,in_right)
            root.left = f(in_left,index-1)
            return root
        return f(0,len(inorder)-1)