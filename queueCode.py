# Queue   -> A nomenclature that lets you allow to access the array in a particular way
# data member: queuesize, array, front, rear
# methods: enqueue(), dequeue(), front(), isFull(), isEmpty(), size()

class Queue:
    def __init__(self, queuesize):
        self.array = []
        self.queuesize = queuesize
        self.front = -1
        self.rear = -1

    def size(self):
        return len(self.array)

    def isEmpty(self):
        if self.size() <= -1:
            return True
        else:
            return False

    def isFull(self):
        if self.size() == self.queuesize:
            return True
        else:
            return False
