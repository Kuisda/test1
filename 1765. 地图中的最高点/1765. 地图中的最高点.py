from typing import List
import numpy as np
from queue import Queue

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        matrix = np.array(isWater)-1
        #ans = [[water - 1 for water in row] for row in isWater]
        q = Queue()

        for i in range(len(isWater)):
            for j in range(len(isWater[i])):
                if isWater[i][j] ==1:
                    q.put((i,j,0))
        while not q.empty():
            posi,posj,val= q.get()
            if posi-1>=0:
                if matrix[posi-1][posj] ==-1:
                    matrix[posi-1][posj]=val+1
                    q.put((posi-1,posj,val+1))
            if posi+1<m:
                if matrix[posi+1][posj] ==-1:
                    matrix[posi+1][posj] =val+1
                    q.put((posi+1,posj,val+1))
            if posj-1>=0:
                if matrix[posi][posj-1] ==-1:
                    matrix[posi][posj-1] =val+1
                    q.put((posi,posj-1,val+1))
            if posj+1<n:
                if matrix[posi][posj+1] ==-1:
                    matrix[posi][posj+1] =val+1
                    q.put((posi,posj+1,val+1)) 
            """
            #说明其实不用val这个组分
            i,j = q.get()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and matrix[x][y] == -1:
                    matrix[x][y] = matrix[i][j] + 1
                    q.append((x, y))
            """        

                    

        return matrix.tolist()


x = Solution()
isWater = [[0,1],[0,0]]
matrix = x.highestPeak(isWater)

print(matrix)