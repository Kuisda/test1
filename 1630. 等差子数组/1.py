from typing import List
class Solution:
    def check(self,nums:List[int])->bool:
        if len(nums)<=2:
            return True
        bios = nums[1]-nums[0]
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]!=bios:
                return False
        return True


    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            subnums = nums[l[i]:r[i]+1]
            subnums.sort()
            if self.check(subnums):
                ans.append(True)
            else:
                ans.append(False)
        return ans

x = Solution()
x.checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5])