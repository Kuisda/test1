from typing import List
from collections import Counter
#滑动窗口
#在s上要找到匹配words的子串，如果匹配则长度需要是len(words[0])*len(words)，移动左下标，右下标就是左下标加上这个长度。
#获取s上的子串后按照words的长度截取并加入到哈希表中
#对比基于words的哈希表，如果两个表中有键以及值的任何不同则说明不能完全匹配。
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        map1 = Counter(words)
        m,n = len(words),len(words[0])
        ls  = len(s)
        i,j = 0,m*n
        ans = []

        for i in range(ls):
            if i+j-1>ls:
                break
            map2 = Counter()
            for k in range(m):
                word = s[i+k*n:i+(k+1)*n]
                map2[word]+=1
            
            flag = True
            for word in words:
                if word not in map2 or map2[word]!=map1[word]:
                    flag = False
                    break
            if flag:
                ans.append(i)
        return ans

