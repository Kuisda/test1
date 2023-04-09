from typing import List
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dict = {}
        for pos,ch in enumerate(s):
            if ch not in dict:
                dict[ch]=pos
            else:
                offset = pos - dict[ch]-1
                if distance[ord(ch)-ord('a')] == offset:
                    continue
                else:
                    return False
        return True
    

x = Solution()
x.checkDistances("abaccb",[1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])