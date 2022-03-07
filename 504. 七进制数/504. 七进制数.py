class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = []
        if num<0:
            flag=True
        else:
            flag=False    
        num =abs(num)
        while 1:
            ans.append(str(num%7))
            num = num//7
            if num==0:
                break

        ans = ''.join(reversed(ans))
        return '-'+ans if flag else ans