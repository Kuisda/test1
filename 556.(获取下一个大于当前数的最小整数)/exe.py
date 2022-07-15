#获取下一个大于当前数的最小整数
#关键取到一个较大数和一个较小数互换，其中较小数的位置要在较大数的左边
#如此，从最右边的数开始向左，一直是递增序列，找到第一个拐点，它的下一个位置就是较小数的位置，也就是找到s[i]<s[i+1]的i
#较大数在[i+1:n]中寻找，要在满足大于较小数的同时尽量小，由于[i+1:n]是递减序列，从n向i+1检索，第一个大于较小数s[i]的就是最小的较大数
#较大较小数交换后还需要将[i+1,n]的降序序列反向，这样才是最小的下一个大于当前数的数
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        i = len(s)-2
        while i >=0:
            if s[i]<s[i+1]: #获取较小数
                break
            i-=1
        if i<0:
            return -1
        j = len(s)-1
        while j>=0 :
            if s[j]>s[i]: #获取较大数
                break
            j-=1
        s[i],s[j] = s[j],s[i] #交换较大，较小数
        s[i+1:] = s[i+1:][::-1] #将[i+1:n]处序列反向
        ans = int(''.join(s))
        return ans if ans <2**31 else -1

x = Solution()
x.nextGreaterElement(12)