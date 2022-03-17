from typing import List
class Trie:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
    def insert(self,word:str)->None:
        node = self      #node指向根结点
        for ch in word:
            ch = ord(ch)-'a'
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True
    def search(self,word:str)->bool:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if node.children[ch] is None or not node.children[ch].isEnd:
                return False
            node = node.children[ch]
        return True        

class Solution:
    def longestWord(self,words:List[str])->str:
        t = Trie()
        for word in words:
            t.insert(word)
        longest = ''
        for word in words:
            if t.search(word) and len(word)>len(longest) or len(word) ==len(longest) and (word<longest):
                longest = word
        return longest        
