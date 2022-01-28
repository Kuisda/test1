from typing import List
import math
def takeFirst(elem):
    return elem[0]

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        ans = 0
        max2 = -1
        properties.sort(key=lambda x:(-x[0],x[1]))#第一维降序第二位升序
        #由于第二维度是升序，所以max2会一直找到第一维度相同的数据中的最大第二维度，而不会出现第二维度更大而第一维度相同的情况
        for i in range(len(properties)):
            if max2>properties[i][1]:
                ans+=1
            else:
                max2 = max(max2,properties[i][1])
        return ans






x = Solution()

MyList = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]

ans = x.numberOfWeakCharacters(MyList)
print(ans)