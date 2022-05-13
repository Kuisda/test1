class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m = len(first)
        n = len(second)
        if m<n:
            return self.oneEditAway(second,first)
        if m>n+1:
            return False
        elif m==n:
            count=0
            for i in range(m):
                if first[i]!=second[i]:
                    count+=1
            return False if count>1 else True
        else:#m=n+1
            if m==1:
                return True
            f1 =0
            s1 =0
            count=0
            while(f1<m and s1<n):
                if first[f1]==second[s1]:
                    f1+=1
                    s1+=1
                elif(count<2):
                    f1+=1
                    count+=1
                else:
                    return False
            return True if count<2 else False#如果first[f1]!=second[s1]发生在first末尾在count+1后会直接跳出循环，这时应该返回False
            
