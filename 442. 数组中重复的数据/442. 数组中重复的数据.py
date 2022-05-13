from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            while nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1] #把nums[nums[i]-1] 与nums[i]的位置换一下就不能完成互换了
        return [num for i,num in enumerate(nums) if num-1!=i]

#遍历num，则将num对应的nums[num-1]加上负号,如果num会出现两次则第二次遇到nums[x-1]的值应该就是负数
#为了防止之前已经加上的负号，所以x要取到绝对值
class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x-1] > 0:
                nums[x-1] = -nums[x-1]
            else:
                ans.append(x)
        return ans

x = Solution()
x.findDuplicates([4,3,2,7,8,2,3,1])