class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        Flist= [1,1]
        num = 2
        ans = 0
        while num<=k:
            Flist.append(num)
            num = Flist[-1]+Flist[-2]
        for point in reversed(Flist):
            if point <= k:
                k -=point
                ans+=1
                if k ==0:
                    return ans    


x = Solution()
print(x.findMinFibonacciNumbers(5))