#数组A[n]中的数据是[0,n-1]相当于一个有向图，从i到A[i]的过程就是一条有向边
#要求找到的集合从出现第一个重复元素后就截止，实际上就是要找一个最大的有向环的长度
#每次找到一个环，记录环的长度后环路径上的所有点就都不用再次访问了，因为都在一个环里面，长度是一样的
from typing import List
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n,ans= len(nums),0
        vis = [False]*n
        for i in range(n):
            cnt = 0
            while not vis[i]:
                vis[i] = True
                i = nums[i]
                cnt+=1
            ans = max(ans,cnt)
        return ans

#这里直接用n来标识已经遍历过的环上的所有点，这样同一个环同样不会重复遍历
class Solution1:
    def arrayNesting(self, nums: List[int]) -> int:
        n,ans= len(nums),0
        for i in range(n):
            cnt = 0
            while nums[i]<n:
                num = nums[i]
                nums[i] = n
                i = num
                cnt+=1
            ans = max(ans,cnt)
        return ans
