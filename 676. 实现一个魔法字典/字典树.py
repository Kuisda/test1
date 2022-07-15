from typing import List

class Trie:
    def __init__(self):
        self.children ={}
        self.isend = False

class MagicDictionary:
    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for s in dictionary:
            node = self.root
            for c in s:
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.isend = True
    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        def dfs(node:Trie,pos:int,modify:bool)->bool:#modify用来标记是否已经有修改
            if pos==n:
                return modify and node.isend #搜索结束，必须要修改过且当前位置处于字典树的一个末尾(匹配到一个串,而不是这个串的子串)才是True
            
            if searchWord[pos] in node.children:
                if dfs(node.children[searchWord[pos]],pos+1,modify):
                    return True

            if not modify:
                for ch in node.children:
                    if ch !=searchWord[pos]: #需要检索每一个pos下如果修改searchWord[pos]后的子串部分能不能匹配
                        if dfs(node.children[ch],pos+1,True):
                            return True
            return False
        return dfs(self.root,0,False)