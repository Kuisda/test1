from typing import List
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Optional 在于可以使用 ==None判断，不然可能会报错
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        maxdepth = 0
        q = deque()
        q.append((root,1))
        while(q):
            node,depth = q.pop()
            if depth<=maxdepth:
                ans[depth-1] = max(ans[depth-1],node.val)
            else:
                maxdepth+=1
                ans.append(node.val)
            if(node.left):
                q.append((node.left,depth+1))
            if(node.right):
                q.append((node.right,depth+1))
        return ans

