from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(0, i):
                # temp = matrix[i][j]
                # matrix[i][j] = matrix[j][i]
                # matrix[j][i] = temp
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            first, last = 0, len(matrix) - 1
            while first < last:
                matrix[i][first], matrix[i][last] = matrix[i][last], matrix[i][first]
                first += 1
                last -= 1

        print(matrix)


if __name__ == '__main__':
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s = Solution()
    s.rotate(mat)
