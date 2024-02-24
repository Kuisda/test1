from bisect import bisect_left
from typing import List,Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        ll = []
        def inorder(root:Optional[TreeNode]):
            if root is None:
                return
            inorder(root.left)
            ll.append(root.val)
            inorder(root.right)
        inorder(root)
        ans = []
        for v in queries:
            maxVal, minVal = -1, -1
            index = bisect_left(ll, v)
            if index != len(ll):
                maxVal = ll[index]
                if ll[index] == v:
                    minVal = ll[index]
                    ans.append([minVal, maxVal])
                    continue
            if index != 0:
                minVal = ll[index - 1]
            ans.append([minVal, maxVal])


        return ans
    

c = Solution()

root = TreeNode(4)
root.right = TreeNode(9)
c.closestNodes(root,[3])