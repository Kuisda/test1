
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n==1:
            return 9
        upper = 10**n-1
        for left in range(upper,upper//10,-1):#由于n位*n位得到的结果位数<=2n，可以只枚举左半部分，也就是n位的数字，
                                              #即：10^n-1 到10^(n-1 ) 
            p,x = left,left
            while x:   #利用x获得p的回文数，p是构造的回文数的左边部分
                p = p*10+x%10
                x//=10
            x = upper
            while x*x>=p:#p就是回文数，x从upper开始，如果p%x=0则存在x，y使得x*y=p
                if p%x ==0:
                    return p%1337
                x-=1        