from typing import Optional
from sortedcontainers import SortedList

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        sl = SortedList([])
        queue = [[root,1]]
        curheight = 1
        sum = 0
        while queue:
            node,height = queue.pop(0)
            if height == curheight:
                sum += node.val
            else:
                curheight = height
                sl.add(sum)
                sum = node.val
            if node.left:
                queue.append([node.left,height+1])
            if node.right:
                queue.append([node.right,height+1])
        sl.add(sum)
        return sl[-k] if k <=len(sl) else -1
    
c = Solution()
root = TreeNode(1)
p = TreeNode(2)
root.left = p
p = TreeNode(3)
root.left.left = p

c.kthLargestLevelSum(root,1)

        