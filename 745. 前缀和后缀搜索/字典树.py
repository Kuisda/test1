#使用两个字典树分别储存前缀和后缀
#另一个难点在于需要记录经过的单词的idx，idx记录的是其父结点的child[c]对应的字符c，经过字符c的单词在words中的idx
#(根节点除外，因为它没有父结点，它记录的是所有插入word在words中的idx)
#所以在搜索的时候也需要在搜索到最底部的结点后再得到idx,这才表示遍历完所有前缀或者后缀后，完整经过该字符串的idx
from typing import List
class Node:
    def __init__(self):
        self.child = {}
        self.idx = []

class Trie:
    def __init__(self):
        self.root = Node()
        self.root_reversed = Node()
    def insert(self,word,indx):
        node = self.root
        node.idx.append(indx)
        node_reversed = self.root_reversed
        node_reversed.idx.append(indx)
        for c in word:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
            node.idx.append(indx)
        for c in word[::-1]:
            if c not in node_reversed.child:
                node_reversed.child[c]  = Node()
            node_reversed = node_reversed.child[c]                          
            node_reversed.idx.append(indx)
    def search(self,pref:str,suff:str)->int:
        node = self.root
        idx_list1 = []
        node_reversed = self.root_reversed
        idx_list2 = []
        for c in pref:
            if c not in node.child:
                return -1
            else:
                node = node.child[c]
        #查询完字符串的所有单词后的idx才是经过目标串的索引
        idx_list1 = node.idx
        
        for c in suff[::-1]:
            if c not in node_reversed.child:
                return -1
            else:
                node_reversed = node_reversed.child[c]
        idx_list2 = node_reversed.idx

        len1,len2 = len(idx_list1),len(idx_list2)
        i,j = len1-1,len2-1
        while i>=0 and j>=0:#从后向前遍历，由于idx的append导致idx大的一定在后面，所以从后向前遍历
            if idx_list1[i]>idx_list2[j]:
                i-=1
            elif idx_list1[i]<idx_list2[j]:
                j-=1
            else:
                return idx_list1[i]
        return -1


class WordFilter:
    def __init__(self, words: List[str]):
        self.Tree = Trie()
        for i,word in enumerate(words):
            self.Tree.insert(word,i)

    def f(self, pref: str, suff: str) -> int:
        return self.Tree.search(pref,suff)

            