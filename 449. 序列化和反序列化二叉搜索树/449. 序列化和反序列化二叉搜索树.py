class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        arr = []
        def preorder(root:TreeNode)->None:
            if root:
                arr.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
        return ','.join(map(str,arr))

#arr[0]根据前序遍历一定是根节点，按照二叉搜索树的规律，小于根节点的一定在左子树，大于根节点的一定在右子树
    def deserialize(self, data: str) -> TreeNode:
        if not data or data=='':
            return None
        arr = list(map(int,data.split(',')))
        root = TreeNode(arr[0])
        left = [x for x in arr if x<arr[0]]
        right= [x for x in arr if x>arr[0]]
        root.left = self.deserialize(','.join(map(str,left)))
        root.right= self.deserialize(','.join(map(str,right)))
        return root
