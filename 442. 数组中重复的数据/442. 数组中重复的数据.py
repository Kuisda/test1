from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            while nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1] #把nums[nums[i]-1] 与nums[i]的位置换一下就不能完成互换了
        return [num for i,num in enumerate(nums) if num-1!=i]

x = Solution()
x.findDuplicates([4,3,2,7,8,2,3,1])