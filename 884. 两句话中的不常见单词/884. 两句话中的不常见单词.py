from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        map = Counter(s1.split())+Counter(s2.split())

        ans = []
        for word,num in map.items():#items()以列表返回可遍历的(键, 值) 元组数组。
            if num ==1:
                ans.append(word)
        return  ans