#求5的数量，5*一个偶数就可以得到一个0，偶数永远是足够的。
#25有两个5,125有三个5...
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num=5
        ans=0
        while num<=n:
            ans+=n//num
            num*=5

        return ans