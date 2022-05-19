#为什么是中位数：
#可以按照升序排序数列，首尾数据形成一组数据对，共有n//2组
#在每组数据中，只要x在数据对的两个数的中间则距离两个数据的距离和就是最少的
#中位数能保证它是每一组数据对的中间
#如果是奇数，取恰好的中间数即可，它一定在所有数据对形成的区间内
from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        med = nums[len(nums)//2]
        ans = 0
        for i,num in enumerate(nums):
            ans += abs(med-num)

        return ans 

