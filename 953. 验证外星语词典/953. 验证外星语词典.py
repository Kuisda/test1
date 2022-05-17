from typing import List
class Solution:#
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={}
        for pos,val in enumerate(order):
            dic[val] = pos
        def compare(a:str,b:str)->bool:#如果全部都是一样的，字符串更长的更大
            n = min(len(a),len(b))
            for i in range(n):
                if dic[a[i]] < dic[b[i]]:
                    return True
                elif dic[a[i]] > dic[b[i]]:
                    return False
            return len(a)<=len(b)
        m = len(words)
        for i in range(m-1):
            if not compare(words[i],words[i+1]):
                return False
        return True
x = Solution()
x.isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz")
                