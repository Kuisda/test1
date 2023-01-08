from typing import List
#startswith用于判断w前缀是否是pref
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)