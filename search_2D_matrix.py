from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if target == matrix[i][j]:
                    return True
                elif i+1 < len(matrix) and target >= matrix[i + 1][0]:
                    i += 1

        return False


if __name__ == '__main__':
    array = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    search = 13
    s = Solution()
    ans = s.searchMatrix(array, search)
    print(ans)
