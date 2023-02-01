from collections import defaultdict


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict = defaultdict()
        key = key.replace(' ','')
        pos = 0
        for i,ch in enumerate(key):
            if ch not in dict:
                dict[ch] = chr(ord('a')+pos)
                pos+=1
        ans = ''
        for ch in message:
            if ch==' ':
                ans+=' '
            else:
                ans+=dict[ch]
        return ans

x = Solution()
x.decodeMessage("the quick brown fox jumps over the lazy dog","vkbs bs t suepuv")