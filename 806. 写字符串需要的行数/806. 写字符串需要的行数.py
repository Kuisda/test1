from typing import List
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        col  = 100
        for ch in s:
            temp = col-widths[ord(ch)-ord('a')]
            if temp>=0:
                col = temp
            else:
                line+=1
                col = 100-widths[ord(ch)-ord('a')]
        return [line,100-col]            