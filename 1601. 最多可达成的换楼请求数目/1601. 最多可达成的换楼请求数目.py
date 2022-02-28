#二进制枚举
#request 数量m小于16,楼数量n<=20则可以进行枚举
#长度为m的二进制串每一位表示一个request，根据位为1或0枚举了所有的request选择情况，枚举所有情况然后找到符合条件的最多请求数
from typing import List
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        for mark in range(1<<len(requests)):#遍历m位二进制所有可能01情况
            count = mark.bit_count()#计数1的数量
            if count<ans:
                continue
            judge_list=[0]*n
            for i,(x,y) in enumerate(requests):
                if mark & (1<<i):     #遍历mark中的每一位（检查此次枚举选取的请求组合是否符合条件）
                    judge_list[x]-=1
                    judge_list[y]+=1
            if all(x==0 for x in judge_list):
                ans = count
        return ans
