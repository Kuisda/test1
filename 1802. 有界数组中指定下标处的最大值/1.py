'''
思路：
1.元素和有一个上限
2.需要使得主要位置越来越大
3.相邻位置元素差值不超过1

可以首先从全1考虑,然后逐步加目标位置的值,每当目标位置要加1,相邻位置都也要加，就是类似一个山峰
但是受到临界的影响,例如index位置加到4,理论上来说index+2这个位置要变成2,但如果index+2不在数组中就不用加了
'''
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        curSum = n
        curIndexNum = 1
        lastIndexNum  = curIndexNum
        while curSum<=maxSum:
            lastIndexNum  = curIndexNum #当跳出循环时的indexNum肯定会导致Sum > maxSum，所以返回前一个indexNum

            curIndexNum+=1
            rightIncrement = curIndexNum-2 if (curIndexNum-2)<(n-1-index) else (n-1-index) #如果curIndexNum为2，则左右侧都不用加，而如果为3，为了满足相邻位置差值为1左右都需要加1
            leftIncrement  = curIndexNum-2 if (curIndexNum-2)<index       else index
            curSum += 1+rightIncrement+leftIncrement 
        
        return lastIndexNum

c = Solution()
c.maxValue(6,1,10)