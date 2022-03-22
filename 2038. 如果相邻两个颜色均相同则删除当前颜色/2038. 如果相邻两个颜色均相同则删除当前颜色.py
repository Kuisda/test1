#由于只能对连续的三个相同字符形成的字符串删去中间的字符，所以BAAABB这种情况下，不可能出现中间的A全部删除然后使得B连接起来的情况
#只需要统计连续相同字符串的长度即可
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = 0
        prech = colors[0]
        Ap = 0
        Bp = 0
        for i,ch in enumerate(colors):
            if prech == ch:
                count+=1

            if prech!=ch or i==len(colors)-1:
                if prech == 'A':
                    if count>=3:
                        Ap+=count-2
                else:
                    if count>=3:
                        Bp+=count-2

                prech = ch
                count = 1        
        return Ap>Bp

x = Solution()
x.winnerOfGame('AAAABBBB')
