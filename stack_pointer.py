# Stack   -> A data-structure that lets you access the elements in LIFO order
# data member: stacksize, array, top_of_stack
# methods: push(), pop(), top(), isFull(), isEmpty(), printStack()

class Stack:
    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.array = [-1] * stacksize
        self.top_of_stack = -1

    def size(self):
        return len(self.array)

    def push(self, ele):
        """checks whether array size equals stack limit, if not pushes the new element into the array"""
        if self.isFull():
            print("Stack full, can't push")
            return
        else:
            self.top_of_stack = self.top_of_stack + 1
            self.array[self.top_of_stack] = ele

    def pop(self):
        """checks whether stack is empty, if not removes the top most element from the stack"""
        if self.isEmpty():
            print("Stack empty, can't pop")
            return -1
        else:
            """it shouldn't just pop the element, but it has to return"""
            last_ele = self.array[self.top_of_stack]
            self.top_of_stack = self.top_of_stack - 1
            return last_ele

    def top(self):
        """Checking whether the stack is empty, if not we return the last element"""
        if self.isEmpty():
            print("Stack empty")
            return -1
        else:
            last_ele = self.array[self.top_of_stack]
            return last_ele

    def isEmpty(self):
        if self.top_of_stack == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top_of_stack == self.stacksize-1:
            return True
        else:
            return False

    def printStack(self):
        print("Current stack: ")
        for i in range(self.top_of_stack, -1, -1):
            print(self.array[i])


if __name__ == '__main__':
    stack = Stack(4)
    stack.pop()
    stack.top()
    stack.push(34)
    stack.push(45)
    stack.push(645)
    stack.push(74)
    stack.push(57)
    print(stack.top())
    stack.pop()
    stack.pop()
    stack.printStack()