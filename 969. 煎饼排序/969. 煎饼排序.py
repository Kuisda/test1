from typing import List
#把当前最大的数移动到最后，然后将排序数组总长缩小一，接下来将新数组的最大值移到新数组的最后。
#把最大数移动到最后需要进行两次煎饼排序

class Solution:
    def part_reverse(self,arr:List[int],k:int)->List[int]:
        low = 0
        high = k-1
        while low<high:
            arr[high],arr[low] = arr[low],arr[high]

            low+=1
            high-=1
        return arr    

    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        ans = []
        for n in range(len(arr),1,-1):
            maxIndex = 0
            for i in range(n):
                if arr[i]>arr[maxIndex]:
                    maxIndex = i
            if maxIndex == n-1:
                continue        
            arr = self.part_reverse(arr,maxIndex+1)
            ans.append(maxIndex+1)
            arr = self.part_reverse(arr,n)
            ans.append(n)
        return ans

x = Solution()
arr = [3,2,4,1]
ans = x.pancakeSort(arr)