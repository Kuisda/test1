
#双向链表+哈希表
#哈希表根据key来访问key对应的node，node保存了key和value信息
#链表的主要优势是便于插入结点
#根据本题的缓存流和容量，需要将最新的操作放在前面，然后删去最旧访问的结点，双向链表能够遍历的完成结点的移动
class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.refresh(node)
        return node.value    

    def put(self, key: int, value: int) -> None:
        node = Node()
        if key in self.cache: #put的key在hashmap中，修改value值并置于表头右边
            node = self.cache[key]
            node.value = value
            self.refresh(node)
        else:#如果容量够，则直接在表头右边插入，否则先删去最尾部的node(tail的左边)
            if len(self.cache) == self.capacity:
                delnode = self.tail.left
                del self.cache[delnode.key]
                self.delete(delnode)

            node = Node(key,value) 
            self.cache[key] = node
            self.add(node)
    
    def refresh(self,node:Node):
        self.delete(node)
        self.add(node)

    def delete(self,node:Node):
        node.right.left = node.left
        node.left.right = node.right


    def add(self,node:Node): #node插入链表表头的右边
        node.right = self.head.right
        node.left = self.head
        self.head.right.left = node
        self.head.right = node






