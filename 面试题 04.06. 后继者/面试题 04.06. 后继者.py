from asyncio.windows_events import NULL

from sqlalchemy import null


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#二叉搜索树左子树所有结点<当前节点<右子树所有结点
#利用二叉搜索树的性质进行，二分查找，每次找到比目标大的节点赋值给ans，然后搜索节点的左子树，这样保证了搜索得到的值是大于且逐步逼近target值的
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        target = p.val
        cnt = root
        ans = None

        while cnt:
            if cnt.val > target:
                ans = cnt
                cnt = cnt.left
            else:
                cnt = cnt.right   
        return ans