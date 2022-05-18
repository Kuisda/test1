#在乘法表(二维表)中查找第k小的数字
#数字x在乘法表中是第几小 =>公式f(x)
#二分查找找到f(x) = k
from bisect import bisect_left
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(m*n),k,key = lambda x:x//n * n +sum(x//i for i in range(x//n+1,m+1)))