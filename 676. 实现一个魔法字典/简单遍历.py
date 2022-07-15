#利用字典将dictionary 按照长度组织，搜索的时候也只需要搜索指定长度的word即可
from typing import List
class MagicDictionary:
    def __init__(self):
        self.dic = {}

    def compare(self,s:str,tar:int)->bool:
        diff = 0
        for i in range(len(s)):
            if s[i]!=tar[i]:
                diff+=1
        return diff==1
    def buildDict(self, dictionary: List[str]) -> None:
        for s in dictionary:
            if len(s) in self.dic:
                self.dic[len(s)].append(s)
            else:
                self.dic[len(s)] = [s]
    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        if n not in self.dic:
            return False
        else:
            llist = self.dic[n]
            for s in llist:
                if self.compare(s,searchWord):
                    return True
            return False

