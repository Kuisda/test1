#深度优先搜索
from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0]*n
        num = 1
        for i in range(n):
            ans[i] = num
            if num*10<=n:
                num*=10
            else:
                while num%10 ==9 or num+1 >n:#当尾数为9或者当前数+1>n时说明当前位的尾数遍历结束了
                    num//=10 
                num+=1
        return ans    