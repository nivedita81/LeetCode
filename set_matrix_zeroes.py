from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == 0:
        #             matrix[i][0] = True
        #             matrix[0][j] = True
        #
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[0][j] == True or matrix[i][0] == True:
        #             matrix[i][j] = 0

        print(matrix)


if __name__ == '__main__':
    array_list = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    s = Solution()
    s.setZeroes(array_list)
