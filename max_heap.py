class Heap:
    """Heap has a size and the list to store all Heap elements"""

    def __init__(self):
        self.size = 0
        self.heapList = [0]

    def getMaximum(self):
        """Since we are considering a MaxHeap here, the maximum element will be at the root"""
        if self.size == 0:
            return -1
        return self.heapList[0]

    def getParent(self, index):
        return index // 2

    def leftChild(self, index):
        return (2 * index) + 1

    def rightChild(self, index):
        return (2 * index) + 2

    def percolateUp(self, i):
        """Here we check until the percolateUp reaches the root, that's why i/2 > 0, also because we are starting from non-leaf nodes
        if the inserted value is greater than it's parent, we are swapping"""
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def percolateDown(self, i):
        """ Here, we need to check whether we've left and right child. Then we are checking whether the root value is greater than
        any of the children, if yes we are swapping and going until the leaf nodes"""
        while i * 2 <= self.size:
            if self.heapList[i] > self.heapList[self.leftChild(i)] or self.heapList[i] > self.heapList[self.rightChild(i)]:
                if self.heapList[i] > self.heapList[self.leftChild(i)]:
                    self.heapList[i], self.heapList[self.leftChild(i)] = self.heapList[self.leftChild(i)], \
                                                                         self.heapList[i]
                    self.percolateDown(self.heapList[self.leftChild(i)])

                elif self.heapList[i] > self.heapList[self.rightChild(i)]:
                    self.heapList[i], self.heapList[self.rightChild(i)] = self.heapList[self.rightChild(i)], \
                                                                          self.heapList[i]
                    self.percolateDown(self.heapList[self.rightChild(i)])
            i = i + 1

    def insertEle(self, k):
        """ here we need not pass k in percolateUp, because we just need the index for percolateUp.
             Hence self.size being the index of the lastly added element, it is passed"""
        self.heapList.append(k)
        self.size = self.size + 1
        self.percolateUp(self.size // 2)
        self.printHeap(self.heapList)

    def printHeap(self, array):
        for i in range(0, len(array)):
            print(array[i])


if __name__ == '__main__':
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    arr_size = len(arr)
    h = Heap();
    for i in range(0, arr_size):
        h.insertEle(arr[i])
