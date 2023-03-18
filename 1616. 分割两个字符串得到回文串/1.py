import math
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a:str, b:str)->bool:
            n = len(a)
            left,right = 0,n-1
            #一个从首部一个从尾部开始匹配
            while left<right and a[left]==b[right]:
                left+=1
                right-=1
            if left>=right:
                return True
            return checkMiddle(a,left, right) or checkMiddle(b,left, right)
        #从头和尾开始的子串匹配遇到不相同字符的下标位置时，如果left<right，还有一种可能会构成子串，就是a[left,right]或者b[left,right]本身也是一个回文串
        def checkMiddle(s:str,left:int,right:int)->bool:
            while left<right and s[left]==s[right]:
                left+=1
                right-=1
            if left>=right:
                return True
            return False

        
        return check(a,b) or check(b,a)



