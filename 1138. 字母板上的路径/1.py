#由于z的位置很特别，为了确保能够成功达到z，需要首先进行左移，这样才能达到z上方；
#为了确保能够成功从z出去，需要首先进行上移。
#所以要先进行左移和上移
from typing import List
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def getLocation(s:str):
            num = ord(s)-ord('a')
            row = num // 5
            col = num % 5
            return (row,col)
        curx,cury=0,0
        ans = []
        for c in target:
            x,y = getLocation(c)
            if curx>x:
                ans.append('U'*(curx-x))
            if cury>y:
                ans.append('L'*(cury-y))
            if curx<x:
                ans.append('D'*(x-curx))
            if cury<y:
                ans.append('R'*(y-cury))
            ans.append('!')
            curx,cury=x,y
        return ''.join(ans)

            
