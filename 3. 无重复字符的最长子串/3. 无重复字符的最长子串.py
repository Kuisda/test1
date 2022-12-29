#双指针，滑动窗口
#j向右探测，当没有遇到已知字母时j一直向右，直到找到第一个遇到已知字母，这时就是一个以i为起点的最大的currentlen，与maxlen对比
#当遇到已知字母时，i一直向右滑动，直到j的右边的一位遇到的已知字母在MAP中被消除为止，然后再此探测j
#有一个关键就是什么时候会出现maxlen，上述的一种maxlen情况是主要的出现情况，还有一种情况就是在j到达数组最右边的时候，此时不会进入判断是否在map的逻辑
#所以还要再用currentlen与maxlen做一次对比
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s=="":
            return 0
        i,j=0,0
        maxlen=1
        currentlen=1
        mymap={s[0]:True}
        while j<len(s)-1:
            if s[j+1] not in mymap:
                j+=1
                mymap[s[j]] = True
                currentlen+=1
            else:
                maxlen = max(maxlen,currentlen)
                while s[j+1] in mymap:
                    mymap.pop(s[i])
                    i+=1
                    currentlen-=1
        maxlen = max(maxlen,currentlen) 
        return maxlen

x = Solution()
x.lengthOfLongestSubstring("abcabcbb")
            