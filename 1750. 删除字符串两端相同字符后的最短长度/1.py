class Solution(object):
    def minimumLength(self, s):
        i,j=0,len(s)-1
        leftii,rightj = i,j
        while(i<j):
            lefti = i#事先保存前缀左边界，因为可能遇到前后缀不匹配的情况，但这个时候i表示的是前缀的右边界，等于把序列剪短了
            while i<len(s)-1 and s[i+1]==s[i]:#找到前缀右边界
                i+=1
            rightj = j
            while j>0 and s[j-1]==s[j]:#找到后缀边界
                j-=1
            if s[i]==s[j]:#比较前后缀字母是否相同
                i+=1
                j-=1
            else:#如果本次前后缀没有匹配成功，则回到前后缀的左边界和右边界
                i = lefti
                j = rightj
                break
            
        if i>j:
            return 0
        else:
            return j-i+1




c = Solution()
s = "aabccabba"
print(c.minimumLength(s))
