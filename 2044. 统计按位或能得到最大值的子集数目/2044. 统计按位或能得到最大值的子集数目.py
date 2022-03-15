#按位或是指对数组中的所有元素依次按位或，对数组[1,2,3]按位或结果为1|2|3
from typing import List
from functools import reduce
from operator import or_
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr, cnt = 0, 0
        for i in range(1, 1 << len(nums)):
            orVal = reduce(or_, (num for j, num in enumerate(nums) if (i >> j) & 1), 0)
            #第一个元素为0，然后对中间的整个list的每一个元素，先与最左边的元素做按位或，结果再与次最左的元素按位或

            if orVal > maxOr:
                maxOr, cnt = orVal, 1
            elif orVal == maxOr:
                cnt += 1
        return cnt

