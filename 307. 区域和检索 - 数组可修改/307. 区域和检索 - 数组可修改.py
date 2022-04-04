#index & -index得到的是当前index二进制的从末尾开始的第一个1
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums, 1):
            self.add(i, num)

    def add(self, index: int, val: int): #将index，val涉及的祖先节点更新
        while index < len(self.tree): 
            self.tree[index] += val
            index += index & -index

    def prefixSum(self, index) -> int: #前缀和计算
        s = 0
        while index:
            s += self.tree[index]
            index &= index - 1
        return s

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)