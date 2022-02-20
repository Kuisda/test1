#直接正向遍历即可，如果是1则必须与后一位连接，pos+2，如果是0则不需要连接，pos+1。
# 如果最后的pos恰好在最后一位上则成立，否则不成立。
from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        pos = 0
        while pos<len(bits)-1:
            if bits[pos]==0:
                pos+=1
                continue
            elif bits[pos]==1:
                pos+=2
                continue
        if pos==len(bits)-1:
            return True
        else:
            return False       

 

