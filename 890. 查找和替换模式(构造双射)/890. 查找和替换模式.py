#构造双射的方式：
#利用哈希表对应a->b，可以通过哈希表检查->方向是否是单射
#利用集合对应a<—b，通过集合检查<-方向是否是单射，也就是检查pattern中是否有元素被使用了两次
from typing import List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        flag = True
        for s in words:
            dict = {}
            sset = set()
            for i,ch in enumerate(s):
                if ch in dict and dict[ch]!=pattern[i]:
                    flag = False
                    break
                if ch not in dict:
                    if pattern[i] in sset:
                        flag = False
                        break
                    sset.add(pattern[i])
                    dict[ch] = pattern[i]
            if flag:
                ans.append(s)
            flag = True
        return ans


x = Solution()
x.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb")