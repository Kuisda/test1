import enum
from itertools import chain
from math import ceil
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):#只有一行或只有一列
            return s

        T = ceil(len(s)/(numRows+numRows-2))
        list = [['']*(T*(numRows-1)) for _ in range(numRows)]
        posx=0
        posy=0
        straight = True
        for i in s:
            list[posx][posy] = i
            if straight:
                posx+=1
            else:
                posx-=1
                posy+=1

            if straight and posx==numRows-1:
                straight =False

            if not straight and posx==0:
                straight = True   
        ans=''

        for i in range(numRows):
            for j in range(len(list[0])):
                ans+=list[i][j]
        # ''.join(ch for row in list for ch in row if ch)

        return ans

#压缩矩阵，创建每行为一个空列表，只用关注行的变化，直接添加到对应行的后面即可
def convert1(self, s: str, numRows: int) -> str:
    if numRows==1 or numRows>=len(s):#只有一行或只有一列
            return s
    list = [[]for _ in range(numRows)]
    pos = 0
    T = numRows+numRows-2
    for i,ch in enumerate(s):
        list[pos].append(ch)
        x+=1 if i % T < numRows -1 else -1#通过周期来确定是不是到行尾
    return ''.join(chain(*list))#chain返回一个迭代器，按照先行后列的顺序遍历这个二维矩阵




x = Solution()
s = x.convert("PAYPALISHIRING",4)        