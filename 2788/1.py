from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            str = ""
            for ch in word:
                if ch == separator:
                    if(str):
                        ans.append(str)
                        str = ""
                else:
                    str += ch
            if str !="":
                ans.append(str)
                str = ""
        return ans
    

c = Solution()
print(c.splitWordsBySeparator(["$easy$","$problem$"],"$"))