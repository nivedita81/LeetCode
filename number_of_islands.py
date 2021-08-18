from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]], gridName: str) -> int:

        row = len(grid)
        col = len(grid[0])

        # print(type(grid[0][0]))
        # print(type(gridName))

        visited = [[False for j in range(col)] for i in range(row)]
        count = 0

        for i in range(0, row):
            for j in range(0, col):
                if visited[i][j] is False and grid[i][j] == "1":
                    self.countIslands(grid, i, j, visited)
                    count += 1

        return count

    def cornerCases(self, grid: List[List[str]], i: int, j: int, visited: List[List[bool]]):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not visited[i][j] and grid[i][j] == "1"

    def countIslands(self, grid: List[List[str]], i: int, j: int, visited: List[List[bool]]):

        rowVal = [0, 0, -1, 1]
        colVal = [-1, 1, 0, 0]

        visited[i][j] = True

        for k in range(0, 4):
            if self.cornerCases(grid, i + rowVal[k], j + colVal[k], visited):
                self.countIslands(grid, i + rowVal[k], j + colVal[k], visited)


if __name__ == '__main__':
    # matrix = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    matrix = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]

    row_val = len(matrix)
    col_val = len(matrix[0])

    s = Solution()
    islands = s.numIslands(matrix, 7)
    print(islands)
