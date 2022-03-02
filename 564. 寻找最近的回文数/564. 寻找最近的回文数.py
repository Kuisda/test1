class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        if num<=10:
            return str(num-1)
        s =n[:len(n)//2+len(n)%2]
        s1 = str(int(s)-1)
        s2 = str(int(s)+1)

        return min(
            '9'*(len(n)-1),
            '1'+'0'*(len(n)-1)+'1',
            s+s[-1-len(n)%2::-1],#前半部分翻转添加，如果是奇数，起始端是s的倒数第二位
            s1+s1[-1-len(n)%2::-1],
            s2+s2[-1-len(n)%2::-1],
            key = lambda x:(abs(int(x)-int(n))or float('inf'),int(x)) #如果abs差值为0就返回一个极大值
            #这里控制的是一个比较元组，如果两个的abs差值相等就选择int(x)比较小的那个
        )


x = Solution()
print(x.nearestPalindromic('11'))              

        