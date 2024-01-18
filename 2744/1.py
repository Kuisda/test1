from ast import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        myset = set()
        ans = 0
        for s in words:
            if s[::-1] in myset:
                ans +=1
                myset.remove(s[::-1])
            else:
                myset.add(s)
        return ans