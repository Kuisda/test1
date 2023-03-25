#从前缀后缀都找非递减序列
#先找后缀非递减序列+前缀序列枚举
#1.right从len(arr-1)移动到后缀非递减序列的最左侧
#2.left从0开始向右扩大非递减序列，同时当arr[left]>arr[right]时，right需要右移，此时需要移除的子数组在left和right之间
#但是当right右移直到过界的时候，就不存在后缀非递减序列了，移除的子数组就变成了left向右的全体
from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left,right = 0,len(arr)-1
        n = len(arr)
        ans = n-1
        while right>0 and arr[right]>=arr[right-1]:
            right-=1
        if left == right: #全符合非递减情况
            return 0
        else:
            ans =right #初始化为前缀全部除去,
        while left<n-1:
            while right<n and arr[left]>arr[right]:
                right+=1
            if right!=n:
                ans = min(right-left-1,ans)
            else:#当arr[left]>right序列中的最大项时后缀都将不满足，
                ans = min(n-left-1,ans)
            if arr[left]<=arr[left+1]:
                left +=1
            else:
                break
        return ans
            
x = Solution()
x.findLengthOfShortestSubarray([5,4,3,2,1])
        