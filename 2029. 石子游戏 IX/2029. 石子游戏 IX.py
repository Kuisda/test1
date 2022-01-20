"""
它们的价值除以3的余数分别为 0, 1, 2.我们可以直接用 0, 1,2 代表它们的价值，对应的石子数量分别为cnt0,cnt1,cnt2.
移除类型0的石子并不会对总和产生影响，因此类型0的石子可以看成是「先后手」交换


"""


from typing import List
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for val in stones:
            if(val%3 == 0):
                cnt0+=1
            elif(val%3 == 1):
                cnt1+=1
            else:
                cnt2+=1
        if(cnt0%2 ==0):
            return cnt1>=1 and cnt2>=1
        return cnt1-cnt2>2 or cnt2-cnt1>2