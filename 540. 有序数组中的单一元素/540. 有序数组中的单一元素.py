from typing import List

#假设只出现一次的元素位于下标x,由于其余每个元素都出现两次，因此下标x 的左边和右边都有偶数个元素，数组的长度是奇数。
#如果mid落在左侧，根据（low+high）/2算得的下标一定是偶数下标，如果出现两次则一定与mid+1下标对应数相等
#如果mid落在右侧，根据（low+high）/2算得的下标一定是奇数下标，如果出现两次也一定与mid-1下标对应数相等
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low <high:
            mid = (low+high)//2 #整数除法
            if nums[mid] == nums[mid^1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]