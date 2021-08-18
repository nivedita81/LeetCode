from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        numOfProvinces = 0
        visited = set()
        for start in range(len(isConnected)):
            if start not in visited:
                numOfProvinces += 1
                dfs(start)

        return numOfProvinces


if __name__ == '__main__':
    isConn = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    output = Solution().findCircleNum(isConn)
    print(output)
