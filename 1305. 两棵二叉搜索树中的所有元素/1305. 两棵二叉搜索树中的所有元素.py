from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        #中序遍历
        def inorder(node:TreeNode,res:List[int]):
            if node:
                inorder(node.left,res)
                res.append(node.val)
                inorder(node.right,res)
        list1,list2=[],[]
        merged = []

        inorder(root1,list1)
        inorder(root2,list2)

        i,j = 0,0
        n1,n2 = len(list1),len(list2)
        #归并，将两个升序的数组合并
        while True:
            if i==n1:
                merged.extend(list2[j:])
                break
            if j==n2:
                merged.extend(list1[i:])
                break
            if list1[i]<list2[j]:
                merged.append(list1[i])
                i+=1
            else:
                merged.append(list2[j])
                j+=1
        return merged
