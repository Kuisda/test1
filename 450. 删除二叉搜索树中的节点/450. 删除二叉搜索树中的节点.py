from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node,prenode = root,None
        while node and node.val!=key:
            prenode = node
            node = node.right if node.val <key else node.left
        if node is None:
            return root
        if node.left is None and node.right is None:
            node = None
        elif node.right is None:#使得prenode链接到node.left
            node = node.left
        elif node.left is None:
            node = node.right
        else:#左右子树都有，选取右子树的最小节点
            nnode,prennode = node.right,node
            while nnode.left:
                prennode = nnode
                nnode = nnode.left

            if prennode.val ==node.val:#对应nnode没有左子树的情况，此时prennode位于初始位置node
                prennode.right = nnode.right#只需要将nnode的右子树接到node的右子树上
            else:
                prennode.left = nnode.right


            nnode.right = node.right
            nnode.left  = node.left
            node = nnode
        if prenode is None:
            return node
        if prenode.left and prenode.left.val == key:
            prenode.left = node
        else:
            prenode.right = node
        return root


        



