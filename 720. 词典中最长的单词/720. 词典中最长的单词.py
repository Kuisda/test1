from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
       words.sort(key=lambda x: (-len(x), x), reverse=True) #字典序的比较排序没有-x
       ans =''
       dic = {''}
       for s in words:
           if s[:-1] in dic:
               ans = s
               dic.add(s)

       return ans       

