from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = []
        for i in range(m):
            partlist = []
            for j in range(n):
                cnt=0
                sum=0
                addlist =[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
                for x,y in addlist:
                    if (x<m and x>=0) and (y<n and y>=0):
                        sum+=img[x][y]
                        cnt+=1
                partlist.append(sum//cnt)        
            ans.append(partlist)
        return ans                
                