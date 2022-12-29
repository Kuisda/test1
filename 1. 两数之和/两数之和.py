from typing import List

"""
思路:排序,哈希表用于记录排序前的val坐标,使用双指针找到目标的两个值

另一个思路是直接用哈希表,遍历一次nums,对nums[i]查看target-nums[i]是否在哈希表中
对比上面的方法缺少了排序,而且空间复杂度是一致的,最后也只需要一次遍历,时间复杂度等于从O(nlogn)降低到了O(n) 
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,val in enumerate(nums):
            if val not in hash:
                hash[val] = [i]
            else:
                hash[val].append(i)
        ans = []
        nums.sort()
        i,j= 0,len(nums)-1
        while i<j:#一定存在某个情况两者相加是target值
            if nums[i]+nums[j]>target:
                j-=1
            elif nums[i]+nums[j]<target:
                i+=1
            else:
                ans.append(hash[nums[i]].pop())
                ans.append(hash[nums[j]].pop())
                break
        return ans

x = Solution()
x.twoSum([3,3],6)



