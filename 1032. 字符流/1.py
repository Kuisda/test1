from typing import List
class Tries:
    def __init__(self):
        self.nums = [None]*26
        self.is_end = False
    def insert(self,s:str):
        node = self
        for ch in s[::-1]:
            pos = ord(ch)-ord('a')
            if node.nums[pos] is None:
                node.nums[pos] = Tries()
            node = node.nums[pos]
        node.is_end = True
    def Search(self,s:str)->bool:
        node = self
        for ch in s[::-1]:
            pos = ord(ch)-ord('a')
            if node.nums[pos] is None:
                return False
            node = node.nums[pos]
            if node.is_end:
                return True
        return False



class StreamChecker:
    def __init__(self, words: List[str]):
        self.tr = Tries()
        for w in words:
            self.tr.insert(w)
        self.charStream = []

    def query(self, letter: str) -> bool:
        self.charStream.append(letter)
        return self.tr.Search(self.charStream[-201:])#每个word长度不超过200，后缀匹配的最大长度也不超过一个word，所以只需要匹配后200个字符
