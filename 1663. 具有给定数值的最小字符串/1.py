#贪心算法,尽量把最大的字母都集中在最后面，这样就保证前面的a是最多的
#前缀和最小串由三个部分组成，前方的a，后方的z以及中间的一个介于a-z之间的字符(这个字符可能会因为k%26==0而不会出现)
#思路是假设初始全是a，然后看按照数值k能加到几个z到末尾
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        count = (k-n)//25#有几个z
        ch_offset=(k-n)%25#中间字符相对于a的偏移
        if ch_offset:#如果有中间字符最后前面增加的a的数量也会变
            ans = chr(ch_offset+ord('a'))+'z'*count
            ans = 'a'*(n-count-1) + ans
        else:
            ans = 'z'*count
            ans = 'a'*(n-count) + ans
        return ans
