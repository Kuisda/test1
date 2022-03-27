from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        all_sum =(len(rolls)+n)*mean
        n_sum = all_sum - sum(rolls)
        ans = []
        if n_sum>6*n or n_sum<1*n:
            return []
        
        quotient, remainder = divmod(n_sum,n)
        return [quotient+1]*remainder+[quotient]*(n-remainder) #首先是ans中n个全是quotient，按照除法的定义对应商下的余数为remainder，则对构造中的remainder个数的商加一，其和就能够达到n_sum
        """
        for i in range(n):
            if i==n-1:
                    ans.append(n_sum)
                    break
            for num in range(6,0,-1):
                if n_sum-num>=n-(i+1):
                    ans.append(num)
                    n_sum-=num
                    break
        """
        return ans

x =Solution()
x.missingRolls([3,2,4,3],4,2)        