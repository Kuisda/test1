class Solution:
    def to_int(self,s:str):
        # real1, imag1 = map(int, num1[:-1].split('+'))
        #int()能够将'1'转换为1
        x = s.split('+')
        minus=0
        weight=1
        a=0
        ai=0
        for num,i in enumerate(x[0]):
            
            if num==0 and i=='-':
                minus = 1
            else:
                a=a*weight+(ord(i)-ord('0'))
                weight*=10
        if minus==1:
            a = -a            
        x[1]=x[1].replace('i','')
        minus=0
        weight=1
        for num,i in enumerate(x[1]):
            if num==0 and i=='-':
                minus = 1
            else:
                ai=ai*weight+(ord(i)-ord('0'))
                weight*=10    
        if minus==1:
                ai = -ai
        return a,ai                        


    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,ai =self.to_int(num1)
        b,bi = self.to_int(num2)

        c = a*b+(-1)*ai*bi
        ci= a*bi+ai*b
        ans = "{}+{}i".format(str(c),str(ci))
        return ans

x=Solution()
x.complexNumberMultiply("1+-1i","1+-1i")
