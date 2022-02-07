class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        AlphaList = [[a,'a'],[b,'b'],[c,'c']]
        while True:
            AlphaList.sort(key=lambda x :-x[0])
            hasNext = False
            for i,(num,ch) in enumerate(AlphaList):
                if num<=0: #因为是降序排列，如果当前num为0后面的num也一定是0
                    break
                if len(ans)>=2 and ans[-2]==ch and ans[-1]==ch:
                    continue
                hasNext = True
                ans.append(ch)
                AlphaList[i][0]-=1
                break
            if not hasNext:
                return ''.join(ans)    

