class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
        #s[a:b:c] a:b表示区间，c表示步长，如果是-1就完成了逆序