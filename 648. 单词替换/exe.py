from typing import List
#字典树
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



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tree = Trie()
        for word in dictionary:
            tree.insert(word)
        words = sentence.split(' ')
        ans = []
        for s in words:
            ans.append(tree.search(s))
        return ' '.join(ans)
