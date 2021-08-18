class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.val) + " -> ")
            temp = temp.next

    def pushList(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node


def addTwoNumbers(l1: ListNode, l2: ListNode):
    result = ListNode(0)
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    t1, t2 = l1.val, l2.val
    carry = 0
    while (l1 is not None) and (l2 is not None) and (carry != 0):
        result.val = (t1 + t2 + carry) % 10
        carry = (t1 + t2 + carry) / 10
        if l1.next is not None:
            t1 = l1.next
        else:
            t1 = None
        if l2.next is not None:
            t2 = l2.next
        else:
            t2 = None

        if result is None:
            result = ListNode(result.val)
        else:
            result.next = ListNode(result.val)
            result = result.next
    return result.next


if __name__ == '__main__':
    list1 = LinkedList()
    list2 = LinkedList()
    res = LinkedList()

    list1.pushList(2)
    list1.pushList(4)
    list1.pushList(3)
    print("List 1:")
    list1.printList()

    list2.pushList(5)
    list2.pushList(6)
    list2.pushList(4)
    print("List 2:")
    list2.printList()

    res = addTwoNumbers(list1, list2)
    res.printList()
