from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return

        row = len(board)
        col = len(board[0])

        visited = [[False for j in range(0, col)] for i in range(0, row)]

        for i in range(0, row):
            for j in range(0, col):
                if (i == 0 or i == row - 1 or j == 0 or j == col - 1) and board[i][j] == 'O' and not visited[i][j]:
                    self.dfs(board, i, j, visited)

        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '$':
                    board[i][j] = 'O'

        print(board)

    def isValid(self, board: List[List[str]], i: int, j: int):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        else:
            return True

    def dfs(self, board: List[List[str]], i: int, j: int, visited: List[List[bool]]):

        if visited[i][j] or not self.isValid(board, i, j):
            return

        board[i][j] = '$'
        visited[i][j] = True

        rowVal = [0, 0, -1, 1]
        colVal = [-1, 1, 0, 0]

        for k in range(0, 4):
            if self.isValid(board, i + rowVal[k], j + colVal[k]):
                if board[i + rowVal[k]][j + colVal[k]] == 'O':
                    self.dfs(board, i + rowVal[k], j + colVal[k], visited)


if __name__ == '__main__':
    matrix = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s = Solution()
    s.solve(matrix)
