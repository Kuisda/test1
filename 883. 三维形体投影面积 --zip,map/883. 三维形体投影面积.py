from typing import List
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(v>0 for row in grid for v in row)
        yz = sum(map(max,zip(*grid)))#可以zip(*)表示解压，返回的是按列分组的元组，map是对序列的每一个部分使用max函数
        xz = sum(map(max,grid))
        return xy+yz+xz
