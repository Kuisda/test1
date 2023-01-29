#field对应的就是斜杠，初始为True，当遇到第一个'|'就变成False，遇到第二个时又变成'True'，这样就过滤掉了位于两个'|'之间的*号
class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        field = True
        for ch in s:
            if ch=='|':
                field = not field
            elif ch=='*' and field:
                ans+=1
        return ans
            
