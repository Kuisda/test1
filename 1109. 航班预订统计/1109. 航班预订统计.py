#差分数组：简而言之就是位置r记录的是原数组a中的a[r]-a[r-1]
#性质：当对一个连续区间[l,r]加一个值val的时候，差分数组对应的改变为：d[l]+val,d[r+1]-val
#之后可以根据差分数组前缀和 得到原数组每个位置的增加后的值

#用于存在连续区间修改的情况
from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0]*n

        for left,right,val in bookings:
            nums[left-1] +=val #因为left从1开始计数所以才要-1
            if right < n:
                nums[right]-=val#同样因为计数起始点原因，不需要right+1


        for i in range(1,n):
            nums[i]+=nums[i-1]
        return nums    


