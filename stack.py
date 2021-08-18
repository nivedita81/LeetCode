# Stack   -> A nomenclature that lets you allow to access the array in a particular way
# data member: stacksize, array
# methods: push(), pop(), top(), isFull(), isEmpty(), size()

class Stack:
    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.array = []

    def size(self):
        return len(self.array)

    def push(self, ele):
        """checks whether array size equals stack limit, if not pushes the new element into the array"""
        if self.isFull():
            print("Stack full, can't push")
            return
        else:
            self.array.append(ele)
            self.printStack()

    def pop(self):
        """checks whether stack is empty, if not removes the top most element from the stack"""
        if self.isEmpty():
            print("Stack empty, can't pop")
            return -1
        else:
            """it shouldn't just pop the element, but it has to return"""
            last_ele = self.array[-1]
            self.array.pop()
            return last_ele

    def top(self):
        """Checking whether the stack is empty, if not we return the last element"""
        if self.isEmpty():
            print("Stack empty")
            return -1
        else:
            last_ele = self.array[-1]
            return last_ele

    def isEmpty(self):
        if self.size() <= 0:
            return True
        else:
            return False

    def isFull(self):
        if self.size() == self.stacksize:
            return True
        else:
            return False

    def printStack(self):
        print("Current stack: ")
        for i in range(0, self.size()):
            print(self.array[i])


if __name__ == '__main__':
    stack = Stack(8)
    stack.push(34)
    stack.push(45)
    stack.push(645)
    stack.push(74)
    stack.push(76)
    stack.push(1)
    stack.push(67)
    stack.push(78)
