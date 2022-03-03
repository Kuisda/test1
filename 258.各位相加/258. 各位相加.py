class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s)>1:
            temp =0
            for ch in s:
                temp +=int(ch)
            s = str(temp)    

        return int(s)



#自然数的数字根与自然数本身 与9同余，要得到一个个位数只需要求自然数除以9的余数。
#但是如果num是9的倍数，最终结果会是9或者0：18的数字根是9，只有为0时数字根才为0
#所以计算num-1除以9的余数，这样保证结果在1-8之间，然后结果加1就可以把倍数的情况纳入到一次除法中，但0还是要另外判断
class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0
