from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [[root,1]]
        swing,curHeight = 1,0 #swing =1 right->left; swing=0 left->right
        ans = []
        while len(queue)!=0:
            node , height = queue.pop(0)
            if height > curHeight:
                ans.append([node.val])
                curHeight = height
                swing = abs(swing - 1)
            else:
                if swing == 0:
                    ans[-1].append(node.val)
                else:
                    ans[-1].insert(0,node.val)
            if node.left != None:
                queue.append([node.left,height+1])
            if node.right != None:
                queue.append([node.right,height+1])
        return ans
            




