from calendar import week
import math

class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        if(n<=7):
            for i in range(1,n+1):
               ans+=i 
        else:
            ans = 28
            week_count = 1
            for i in range(2,math.floor(n/7)+1):
                ans+=28+week_count*7
                week_count+=1   
            week_count+=1    
            for i in range(0,n%7):
                ans+= week_count+i
        return ans

       
x = Solution()
num = x.totalMoney(26)
print(num)