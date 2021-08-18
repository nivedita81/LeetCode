# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def pushList(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        stack = []
        isPalin = False

        while temp is not None:
            stack.append(temp.val)
            temp = temp.next

        temp = head
        for i in range(len(stack) - 1, -1, -1):

            if stack[i] == temp.val:
                temp = temp.next
                isPalin = True
            else:
                isPalin = False
                break
        return isPalin


if __name__ == '__main__':
    lllist = Solution()
    lllist.pushList(3)
    lllist.pushList(7)
    lllist.pushList(4)
    lllist.pushList(2)
    lllist.pushList(8)
    lllist.pushList(12)

    obj = Solution()
    obj.isPalindrome(lllist)
