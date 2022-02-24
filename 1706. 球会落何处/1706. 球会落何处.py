from typing import List
#根据grid在当前列的值确定是左移动还是右移动，然后判断当前位置的形状，如果是v形或者是某个墙，则停止
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1]*n

        for j in range(n):
            col = j
            for row in grid:
                dir = row[col]
                col +=dir
                if col<0 or col==n or row[col] != dir:
                    break
            else:
                ans[j] = col


        return ans