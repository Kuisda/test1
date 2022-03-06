from typing import List
#两个list分别记录当前位置是第几个连续单增或单减的位置

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        down_list = [0]*len(security)
        up_list = [0]*len(security)
        ans = []

        for i in range(1,len(security)):
            if security[i]<=security[i-1] :
                down_list[i] = down_list[i-1]+1
            else:
                down_list[i] = 0
        for j in range(len(security)-2,-1,-1):
            if security[j]<=security[j+1]:
                up_list[j]=up_list[j+1]+1
            else:
                up_list[j] = 0            
        for i in range(len(security)):
            if down_list[i]>=time and up_list[i]>=time:
                ans.append(i)

        return ans            


