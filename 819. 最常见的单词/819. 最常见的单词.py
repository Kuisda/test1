from typing import List
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        freq = Counter()
        word, n = "", len(paragraph)
        for i in range(n + 1):
            if i < n and paragraph[i].isalpha():
                word += paragraph[i].lower()
            elif word:
                if word not in ban:
                    freq[word] += 1
                word = ""
        maxFreq = max(freq.values())
        return next(word for word, f in freq.items() if f == maxFreq)

x = Solution()
print(x.mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))

#因为有用标点符号分隔的有用空格分隔的所以这个方法不太行

class Solution1:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in ['!','?',"'",',',";","."]:
            paragraph = paragraph.replace(i,'')
        paragraph=paragraph.lower()
        dic = Counter(paragraph.split(' '))
        banlist = set(banned)
        max = 0
        maxkey=''
        for (key,value) in dic.items():
            if value>max and key not in banlist:
                maxkey=key
                max = value
        return maxkey