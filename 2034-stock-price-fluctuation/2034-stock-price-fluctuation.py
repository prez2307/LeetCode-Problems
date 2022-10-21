class StockPrice:

    def __init__(self):
        self.myDict = dict()
        self.highestTime = 0
        self.maxHeap = []
        self.minHeap = []

    def update(self, timestamp: int, price: int) -> None:
        self.myDict[timestamp] = price
        self.highestTime = max(self.highestTime, timestamp)
        
        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.myDict[self.highestTime]

    def maximum(self) -> int:
        while self.maxHeap and self.myDict[self.maxHeap[0][1]] != -self.maxHeap[0][0] :
            heappop(self.maxHeap)
        
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        
        while self.minHeap and self.myDict[self.minHeap[0][1]] != self.minHeap[0][0] :
            heappop(self.minHeap)
        
        return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()