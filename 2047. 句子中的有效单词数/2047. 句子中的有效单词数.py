from string import punctuation

#有样例通过不了但不知道为什么
class Solution:
    def isLetter(self,s)-> bool:
        if ord(s)>=ord('a') and ord(s)<=ord('z'):
            return True
        return False    
    def check(self,str) -> bool:
        connect_sign=0
        if len(str)==0:
            return False
        else:
            if str[0] =='-' or str[-1] == '-':
                return False
            for pos,i in enumerate(str):
                if i!=str[-1]:
                    if not (self.isLetter(i)):
                        if i=='-':
                            if connect_sign==1 or not(self.isLetter(str[pos-1]) and self.isLetter(str[pos+1])):
                                return False
                            else:
                                connect_sign=1
                        else:
                            return False        
                else:
                    if not(i in ['!',',','.'] or self.isLetter(i)):   
                        return False         
        return True                    


    def countValidWords(self, sentence: str) -> int:
        ans = 0
        sentenceList = sentence.split(' ')
        for str in sentenceList:
            if(self.check(str)):
                ans+=1
        return ans
""""
class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(s: str) -> bool:
            hasHyphens = False
            for i, ch in enumerate(s):
                if ch.isdigit() or ch in "!.," and i < len(s) - 1:
                    return False
                if ch == '-':
                    if hasHyphens or i == 0 or i == len(s) - 1 or not s[i - 1].islower() or not s[i + 1].islower():
                        return False
                    hasHyphens = True
            return True

        return sum(valid(s) for s in sentence.split())
"""


"""
class Solution:
    def countValidWords(self, sentence: str) -> int:
        arr = sentence.split()
        cnt = 0

        for word in arr:
            # 两种匹配模式，「 | 」 左边为有连接号的更长匹配，右边仅为单词与标点符号的匹配
            # +匹配一至多次，?匹配0到1次，*匹配0到多次
            p = re.match(r'[a-z]+-?[a-z]+[!.,]?|[a-z]*[!.,]?', word)
            if p and p.group(0) == word:
                cnt += 1
        
        return cnt
"""