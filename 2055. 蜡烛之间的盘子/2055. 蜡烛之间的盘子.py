import enum
from typing import List
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        前缀处理的方式不好,用len==s的长度来看
        ans = []
        isolation = []
        sum = 0
        for i,ch in enumerate(s):
            if ch=='|':
                sum+=1
                isolation.append((i,sum))
        if len(isolation)==0:
            for i in range(len(queries)):
                ans.append(0)
            return ans

        for (left,right) in queries:
            left_sum,right_sum=0,0
            for (pos,num) in isolation:
                if pos>=left:
                    left = pos
                    left_sum = num
                    break
            for i in range(len(isolation)-1,-1,-1):
                if isolation[i][0]<=right:
                    right = isolation[i][0]
                    right_sum = isolation[i][1]
                    break
            if left>=right:
                ans.append(0)
            else:
                ans.append((right-left-1)-(right_sum-left_sum-1))        
        return ans
        """
        n = len(s)
        sumlist,sum= [0]*n,0 #任意位置处*的前缀数量和
        left,l = [0]*n,-1 #左侧最近'|'
        for i,ch in enumerate(s):
            if ch=='*':
                sum+=1
            else:
                l = i

            sumlist[i] = sum
            left[i] = l

        right,r = [0]*n,-1 #右侧最近'|'
        for i in range(n-1,-1,-1):
            if s[i]=='|':
                r = i
            right[i] = r

        ans = [0]*len(queries)
        for i,(x,y) in enumerate(queries):
            x = right[x] #左侧的pos取右边最近的'|'
            y = left[y]
            if x>=0 and y>=0 and x<y:
                ans[i] = sumlist[y] - sumlist[x]
        return ans                    





x = Solution()
print(x.platesBetweenCandles("***|**|*****|**||**|*",[[1,17],[4,5],[14,17],[5,11],[15,16]]))