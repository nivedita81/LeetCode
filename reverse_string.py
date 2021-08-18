# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front, back = 0, len(s) - 1
        while front < back:
            s[front], s[back] = s[back], s[front]
            front = front + 1
            back = back - 1

        print(s)


if __name__ == '__main__':
    # input_arr = ["h", "e", "l", "l", "o"]
    input_arr = ["H", "a", "n", "n", "a", "h"]
    sol = Solution()

    sol.reverseString(input_arr)
