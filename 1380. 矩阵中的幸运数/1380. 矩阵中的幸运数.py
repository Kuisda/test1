from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        minRow=[min(row) for row in matrix]
        minCol=[max(col) for col in zip(*matrix)]#与zip相反，用来把每行的第x个元素解压成第x个元组，实现列元组

        for i,row in enumerate(matrix):
            for j,x in enumerate(row):
                if x == minRow[i] ==minCol[j]:
                    ans.append(x)
            

        return ans