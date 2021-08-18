# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = None
        self.next = None

    def pushList(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse_list(self, head: ListNode):
        if head is None or head.next is None:
            return

        previous, next_pointer = None, None
        current = head
        while current is not None:
            next_pointer = current.next
            current.next = previous
            previous = current
            current = next_pointer
        return previous

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        '''here we are getting the middle element to reverse and setting the next pointer of last ele of 1st half to be null'''
        slow = head
        fast = head.next
        # prev = None
        while fast is not None and fast.next is not None:
            # prev = slow
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        '''reversing the 2nd half of the list'''
        second_half = self.reverse_list(second_half)

        first_node = head
        second_node = second_half

        '''combining both the halves'''
        while first_node is not None and second_node is not None:
            first_next = first_node.next
            second_next = second_node.next
            first_node.next = second_node
            second_node.next = first_next

            first_node = first_next
            second_node = second_next



if __name__ == '__main__':
    list_node = Solution()
    list_node.pushList(3)
    list_node.pushList(7)
    list_node.pushList(4)
    list_node.pushList(2)
    list_node.pushList(8)
    list_node.pushList(12)
    list_node.pushList(11)

    s = Solution()
    s.reorderList(list_node)
