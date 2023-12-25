from typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        presum = [0]
        cursum=0
        for i in range(n):#获得前缀和数组
            cursum += 1 if hours[i]>8 else -1
            presum.append(cursum)

        ans = 0
        stack=[]
        for i in range(len(presum)):#一个按照前缀和单调递减的栈，因为要找的是区间和大于0情况下的最大区间，也就是区间[i,j]要有presum[j]-presum[i]>0
            #思考一个确定左端点i的问题，假设posi1在posi2的左边，但posi2的presum值还要比posi1大，则posi2肯定不能成为左端点，因为如果posi2满足presum[j]-presum[i]>0条件，则posi1肯定也满足且长度更长
            #所以从左往右扫描只能取递减的，然后再从后往前遍历右端点即可
            if not stack or presum[stack[-1]]>presum[i]:
                stack.append(i)
        i = n
        while i>ans:
            while stack and presum[stack[-1]]<presum[i]:
                ans = max(ans,i-stack[-1])
                stack.pop()
            i-=1

    
        return ans

x = Solution()
x.longestWPI([9,9,6,0,6,6,9])


