class Trie:
    def __init__(self):
        self.children = [None]*26
        self.end = False
    def insert(self,word)->bool:
        node = self
        for c in word:
            idx = ord(c)-ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.end = True
    def search(self,word):
        node = self
        res = ''
        for c in word:
            idx = ord(c)-ord('a')
            if not node.children[idx]:
                return word
            else:
                res+=c
                node = node.children[idx]
                if node.end:
                    return res
        return word
##使用字典结构可以避免创建多余的空间，而是用到一个字母就创建一个用于储存该字母的对应空间
class Trie1:
    def __init__(self):
        self.children = {}
        self.end = False
    def insert(self,word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie1()
            node = node.children[c]
        node.end = True #使用一个标识符来表示此处是末尾
    def search(self,word):
        node = self
        res = ''
        for c in word:
            if c not in node.children:
                return word
            else:
                res+=c
                node = node.children[c]
                if node.end:
                    return res
        return word

