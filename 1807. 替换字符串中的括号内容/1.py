from typing import List
from collections import defaultdict
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dic = dict(knowledge)
        ans=[]
        start=-1
        for i,ch in enumerate(s):
            if ch=='(':
                start=i
            elif ch==')':
                ans.append(dic.get(s[start+1:i],'?'))
                start = -1
            elif start<0:
                ans.append(ch)
        return "".join(ans)
            
