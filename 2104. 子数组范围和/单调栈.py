#为了使子数组的最小值或最大值唯一，
# 我们定义如果 nums[i] = nums[j]，nums[i]=nums[j]，
# 那么 nums[i]与 nums[j] 的逻辑大小由下标 i 与下标 j 的逻辑大小决定，
# 即如果 i < j，那么 nums[i] 逻辑上小于 nums[j]


from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        minLeft,maxLeft = [0]*n,[0]*n
        minstack,maxstack = [],[]

        for i,num in enumerate(nums): #minLeft[i]记录的是nums[i]左侧最近的比nums[i]小的位置下标
            while minstack and nums[minstack[-1]] > num:
                minstack.pop()
            minLeft[i] = minstack[-1] if minstack else -1
            minstack.append(i)    

        for i,num in enumerate(nums):
            while maxstack and nums[maxstack[-1]] <= num:
                maxstack.pop()
            maxLeft[i] = maxstack[-1] if maxstack else -1
            maxstack.append(i)

        minRight,maxRight = [0]*n,[0]*n
        minstack,maxstack=[],[]
        for i in range(n-1,-1,-1):
            num = nums[i]
            while minstack and nums[minstack[-1]] >=num:#逻辑大于
                minstack.pop()
            minRight[i] = minstack[-1] if minstack else n
            minstack.append(i)

            while maxstack and nums[maxstack[-1]] < num:
                maxstack.pop()
            maxRight[i] = maxstack[-1] if maxstack else n
            maxstack.append(i)

        sumMax,sumMin = 0,0
        #假设nums[i]左侧最近的比nums[i]小的数为nums[j]，右侧最近比它小的数是nums[k]
        #那么以nums[i]为最小值的子数组数目为（k-i）*（i-j）
        for i,num in enumerate(nums):
            sumMax+=(maxRight[i]-i)*(i-maxLeft[i])*num
            sumMin+=(minRight[i]-i)*(i-minLeft[i])*num    
        return sumMax-sumMin