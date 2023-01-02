from typing import List
import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        #(price, amount, orderType)
        buy = []#大顶堆,[price,amount]形式进行存储
        sell= []#小顶堆
        for i in range(len(orders)):#for price, amount, type in orders:
            if orders[i][2]==0: #buy
                #先看sell中是否有能够匹配的，然后再插入优先队列
                while len(sell)!=0 and orders[i][0]>=sell[0][0] and orders[i][1]>0:
                    if orders[i][1] < sell[0][1]:#如果当前的buy订单数量比当前堆顶的sell少，直接减去，且不用添加到积压订单
                        sell[0][1]-=orders[i][1]
                        orders[i][1] = 0 
                        break
                    orders[i][1] -= heapq.heappop(sell)[1] #如果比当前堆顶的sell多，则只是在buy上减去这一部分,同时pop出堆顶元素
                if orders[i][1]:#若剩下无法匹配的当前buy订单，则添加到积压订单
                    heapq.heappush(buy,[-orders[i][0],orders[i][1]])#因为要构建大顶堆所以取负
            else:#sell
                #先看buy中是否有匹配的，然后再插入优先队列
                while len(buy)!=0 and orders[i][0]<=-buy[0][0] and orders[i][1]>0:
                    if orders[i][1] < buy[0][1]:
                        buy[0][1]-=orders[i][1]
                        orders[i][1] = 0
                        break
                    orders[i][1] -= heapq.heappop(buy)[1]
                if orders[i][1]:
                    heapq.heappush(sell,[orders[i][0],orders[i][1]])
        return (sum(x for _,x in buy)+sum(y for _,y in sell))%(10**9 + 7)


c = Solution()
c.getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]])
