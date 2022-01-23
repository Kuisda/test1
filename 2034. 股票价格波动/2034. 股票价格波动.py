from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.priceList = SortedList()#有序列表，默认升序
        self.map = {}
        self.newest = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.map:
            self.priceList.remove(self.map[timestamp])
            self.priceList.add(price)
            self.map[timestamp] = price
        
        else: 
            self.priceList.add(price)
            self.map[timestamp] = price
            if self.newest < timestamp:
                self.newest = timestamp    

    def current(self) -> int:
        return self.map[self.newest]

    def maximum(self) -> int:
        return self.priceList[-1]

    def minimum(self) -> int:
        return self.priceList[0]
