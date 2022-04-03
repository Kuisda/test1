from bisect import bisect_right
from typing import List
import _bisect
#bisert_right(a,b)返回元素b按当前顺序插入到list a 中的位置，b是有序列表
#bisert_right 和bisert_left的区别在于在遇到相同元素的时候，bisert_right会返回b到该元素右边的位置，bisert_left则是左边
#用到了二分查找
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters,target)%len(letters)]