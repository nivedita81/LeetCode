from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:

        m = len(A)
        n = len(A[0])

        if m == n:
            for i in range(len(A)):
                for j in range(0, i):
                    A[i][j], A[j][i] = A[j][i], A[i][j]
        else:
            result = [[None] * m for i in range(n)]
            for i in range(len(A[0])):
                for j in range(len(A)):
                    result[i][j] = A[j][i]
            return result

        return A


if __name__ == '__main__':
    result_matrix = []
    # mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat = [[1,2,3],[4,5,6]]
    s = Solution()
    result_matrix = s.transpose(mat)
    print(result_matrix)
