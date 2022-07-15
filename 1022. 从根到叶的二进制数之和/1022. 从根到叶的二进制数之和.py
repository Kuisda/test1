from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Optional 表示可选，可以不传入这个参数，如果不传入则该参数对应None
class Solution1:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node:Optional[TreeNode],val:int):
            if node is None:
                return 0
            val = (val<<1)|node.val
            if node.left is None and node.right is None:
                return val
            return dfs(node.left,val)+dfs(node.right,val)
        return dfs(root,0)


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        nums = []
        def preorder(node:Optional[TreeNode],num:int):
            if node:
                num = (num<<1)|node.val
                preorder(node.left,num)
                preorder(node.right,num)
            else:
                nums.append(num)
        preorder(root,0)
        return nums
        return int(sum(nums)/2)
