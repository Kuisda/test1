from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        n = len(arr)
        mindis = float('inf')
        for i in range(0,n-1):
            if (arr[i+1]-arr[i])<mindis:
                ans = []
                mindis = arr[i+1]-arr[i]
                ans.append([arr[i],arr[i+1]])
            elif (arr[i+1]-arr[i])==mindis:
                ans.append([arr[i],arr[i+1]])
        return ans
            

x = Solution()
x.minimumAbsDifference([4,2,1,3])