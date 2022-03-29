class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def slidingWindow(ch:str)->int:
            ans,left,sum = 0,0,0
            for right in range(len(answerKey)):
                if answerKey[right]!=ch:
                    sum+=1
                while sum>k:
                    if answerKey[left]!=ch:
                        sum-=1
                    left+=1
                ans = max(ans,right-left+1)
            return ans
        return max(slidingWindow('T'),slidingWindow('F'))            
                    