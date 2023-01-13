from collections import Counter
#本题使用的是模拟的方法
#比较好的思路是思考临界情况，将s,target都转化为dict的形式后，对s，target中的同一字符c,ch，造成的制约是c/ch，显然最终的可形成副本数是c/ch的最小值
#这个是答案的做法
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d = Counter(s)
        ans = 0
        out = False
        while 1:
            for ch in target:
                if ch not in d:
                   out = True
                   break
                else:
                    d[ch]-=1
                    if d[ch]==0:
                        d.pop(ch) 
            if out:
                break
            else:
                ans+=1
        return ans

c = Solution()
c.rearrangeCharacters("ilovecodingonleetcode","code")
