class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def pushList(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def getCount(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count

if __name__ == '__main__':
    lllist = LinkedList()
    lllist.pushList(3)
    lllist.pushList(7)
    lllist.pushList(4)
    lllist.pushList(2)
    lllist.pushList(8)
    lllist.pushList(12)

count = lllist.getCount()
print(count)