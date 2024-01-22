class Solution:
    def maximumSwap(self, num: int) -> int:
        sStr = str(num)
        sSortedList = sorted(list(sStr))
        changePos = 0
        for i in range(len(sSortedList)-1,-1,-1):
            if sStr[changePos] == sSortedList[i]:
                changePos +=1
            else:
                for j  in range(len(sStr)-1,-1,-1):
                    if sStr[j] == sSortedList[i]:
                        sList = list(sStr)
                        sList[changePos],sList[j] = sList[j],sList[changePos]
                        sStr = ''.join(sList)
                        return int(sStr)
        return int(sStr)                

c = Solution()
print(c.maximumSwap(2736))
                
            

        

        
