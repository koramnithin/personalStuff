class Heap(object):
    size = 0
    mh = []
    pos = 0
    def __init__(self,size):
        self.size = size
        self.mh = [None] * (size+1)
        self.pos = 0

    def createHeap(self,arr):
        for i in arr:
            self.insert(i)

    def insert(self,e):
        if self.pos == 0:
            self.mh[self.pos+1] = e
            self.pos = 2
        else:
            self.mh[self.pos] = e
            self.pos += 1
            self.heapifyUp()

    def heapifyUp(self):
        p = self.pos - 1
        while p > 0 and self.mh[p//2] > self.mh[p]:
            y = self.mh[p]
            self.mh[p]=self.mh[p//2]
            self.mh[p//2] = y
            p = p//2

    def extractMin(self):
        m = self.mh[1]
        self.mh[1] = self.mh[self.pos - 1]
        self.mh[self.pos - 1] = 0
        self.pos -= 1
        self.sinkdown(1)
        return m

    def sinkdown(self,k):
        a = self.mh[k]
        m = k
        if 2*k < self.pos and self.mh[m] > self.mh[2*k]:
            m = 2*k
        if 2*k+1 < self.pos and self.mh[m] > self.mh[2*k+1]:
            m = 2*k+1
        if m != k:
            self.swap(m,k)
            self.sinkdown(m)


    def swap(self,a,b):
        temp = self.mh[a]
        self.mh[a] = self.mh[b]
        self.mh[b] = temp

m = Heap(9)
m.createHeap([3,2,1,7,8,4,10,16,12])
print(m.mh)
for i in range(9):
    print(m.extractMin())