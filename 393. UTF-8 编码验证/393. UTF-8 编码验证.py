from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        mask1,mask2 = 1<<7,(1<<7) | (1<<6)

        def getType(num:int) ->int:
            if (num&mask1) ==0:
                return 1

            n,mask = 0,mask1
            while num&mask:
                n+=1
                if n>4:
                    return -1
                mask >>=1
            return n if n>=2 else -1

        index,m = 0,len(data)
        while index < m:
            n = getType(data[index])
            if n<0 or index+n > m or any((ch & mask2) != mask1 for ch in data[index+1:index+n]):
                return False
            index +=n
        return True                    


