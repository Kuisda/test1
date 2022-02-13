from collections import defaultdict
from collections import Counter
from math import floor

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = float('inf')
        dic = defaultdict(int)
        dic['b']=0
        dic['a']=0
        dic['l']=0
        dic['o']=0
        dic['n']=0
        for ch in text:
            if ch in dic:
                dic[ch]+=1
        
        for ch,num in dic.items():
            if ch=='l' or ch=='o':
                if ans>floor(num/2):
                    ans = floor(num/2)
            else:
                if ans >num:
                    ans = num        


        return ans
class Solution2:#和solution1的消耗是一样的
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = Counter(text)
        return min(dic['b'],dic['a'],dic['n'],floor(dic['l']/2),floor(dic['o']/2))



x = Solution()
ans = x.maxNumberOfBalloons("nlaebolko")
print(ans)