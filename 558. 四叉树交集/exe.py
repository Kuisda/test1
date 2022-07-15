from sqlalchemy import intersect


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
#分治法，按照上下左右进行分治
#如果当前节点node1是叶子节点，如果node1 = 1 node1|node2 = node1,否则node1|node2 = node2
#如果node2是叶子节点，结果就相当于将上面的node1与node2交换位置
#如果两者都不是叶子节点，分别对上下左右子树进行分治，然后合并节点，如果上下左右节点都是叶子节点且val相同则合并为叶子节点

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return Node(True,True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return self.intersect(quadTree2,quadTree1)
        o1 = self.intersect(quadTree1.topLeft,quadTree2.topLeft)
        o2 = self.intersect(quadTree1.topRight,quadTree2.topRight)
        o3 = self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
        o4 = self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)

        if o1.isLeaf and o2.isLeaf and o3.isLeaf and o4.isLeaf and o1.val==o2.val==o3.val==o4.val:
            return Node(o1.val,True)
        return Node(False,False,o1,o2,o3,o4)





            

