class Solution:
    def greatestLetter(self, s: str) -> str:
        big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        small='abcdefghijklmnopqrstuvwxyz'
        for i in range(1,27):
            if big[-i] in s and small[-i] in s:
                return big[-i]
        return ''


