# Definition for a binary tree node.
from typing import Optional

#贪心+dfs，以x位界限可以将一个二叉树分为三个子树，x的左子树，右子树以及包含x父节点的剩余节点构成的子树
#由于玩家只能在开始染色的位置的左右子节点和父节点继续染色，所以y玩家选择包含最多节点的子树中最靠近x节点的节点染色是最佳的情况
#注意(左,右,父)这个集合y不可能选择一个以上，因为y玩家也只能染色相邻节点
#所以y玩家染色的最大节点数就是y = max(xleft,xright,n-1-xleft-xright),x则是n-y
#y胜利条件是y>n-y => 2*y>n
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        xleft,xright=0,0
        def dfs(node:Optional[TreeNode])->int:
            if node is None:
                return 0
            lc = dfs(node.left)
            rc = dfs(node.right)
            if node.val==x:#在dfs的过程中顺便确定x对应的node位置，此时x的左右子树中节点数量已经确定
                nonlocal xleft,xright#nonlocal是指出用在函数外的两个变量
                xleft,xright=lc,rc
            return 1+lc+rc
        dfs(root)
        return max(xleft,xright,n-1-xleft-xright)*2>n