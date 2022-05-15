from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxS = 0
        n = len(points)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    #三点求三角形面积公式|1/2[x1(y2-y3)+x2(y3-y1)+x3(y1-y2)]|
                    S = abs(0.5*(points[i][0]*(points[j][1]-points[k][1])+points[j][0]*(points[k][1]-points[i][1])+points[k][0]*(points[i][1]-points[j][1])))
                    if S>maxS:
                        maxS = S
        return maxS

x = Solution()
x.largestTriangleArea([[1,0],[0,0],[0,1]])