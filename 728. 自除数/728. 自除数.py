from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(num:int)->bool:
            s = str(num)
            if s.find('0')!=-1:
                return False
            for ch in s:
                if num%(int(ch))!=0:
                    return False
            return True 

        ans = []
        for num in range(left,right+1):
            if check(num):
                ans.append(num)

        return ans               

x = Solution()
x.selfDividingNumbers(1,22)