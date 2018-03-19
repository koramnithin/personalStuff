from heapq import *
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h1 = []
        self.h2 = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.h1) == len(self.h2):
            maximum = -heappushpop(self.h1, -num)
            heappush(self.h2, maximum)
        else:
            small = heappushpop(self.h2, -num)
            heappush(self.h1, small)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.h1)== len(self.h2):
            return (self.h1[0]+self.h2[0])/2
        else:
            return self.h2[0]



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
param_2 = obj.findMedian()
print(param_2)