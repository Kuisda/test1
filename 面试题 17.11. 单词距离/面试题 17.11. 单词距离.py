from typing import List
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        pre1,this1,pre2,this2 = -1,-1,-1,-1
        mlen = len(words)
        for i,num in enumerate(words):
            if num==word1:
                pre1 = this1
                this1 = i
                if pre2 != -1:
                    mlen = min(mlen,abs(this1-pre2))
                if this2 !=-1:
                    mlen = min(mlen,abs(this1-this2))
            if num==word2:
                pre2 = this2
                this2 = i
                if pre1!= -1:
                    mlen = min(mlen,abs(this2-pre1))
                if this1!= -1:
                    mlen = min(mlen,abs(this2-this1))
        return mlen

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans = len(words)
        index1, index2 = -1, -1
        for i, word in enumerate(words):#两个index每改变一次就做一次减法即可。
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
            if index1 >= 0 and index2 >= 0:
                ans = min(ans, abs(index1 - index2))
        return ans



