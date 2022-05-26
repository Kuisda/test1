from typing import List
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = len(positions)
        height = [0]*n
#判断第i个方块落下后可能的最大高度，如果落在之前的[0,i-1]中的方块j上，则加上j的高度
        for i,(left,size) in enumerate(positions):
            right = left+size-1
            height[i] = size
            for j in range(i):
                leftd,rightd = positions[j][0],positions[j][0]+positions[j][1]-1
                if right >= leftd and left<=rightd:
                    height[i] = max(height[i],height[j]+size)
        for i in range(1,n):
            height[i] = max(height[i],height[i-1]) #有可能此块落下后由于没有堆叠使得比原来的最大高度小
        return height
