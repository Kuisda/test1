class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left=0
        right= len(s)-1
        ans = list(s)
        while left<right:
            if not ans[left].isalpha():
                left+=1
            if not ans[right].isalpha():
                right-=1
            if ans[left].isalpha() and ans[right].isalpha():     
                ans[left],ans[right] = ans[right],ans[left]
                left+=1
                right-=1



        return ''.join(ans)