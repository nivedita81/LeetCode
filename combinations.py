from typing import List
from copy import deepcopy


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp, res = [], []
        if n == 0 or k == 0:
            return [[]]
        if n == 1:
            return [[n]]
        self.dfs(n, k, 1, 0, temp, res)
        return res

    def dfs(self, n: int, k: int, curr_num: int, curr_len: int, temp: List[int], res: List[List[int]]):
        if curr_len == k:
            temp_copy = deepcopy(temp)
            res.append(temp_copy)
            return
        else:
            for i in range(curr_num, n+1):
                temp.append(i)
                self.dfs(n, k, i+1, curr_len+1, temp, res)
                temp.pop()


if __name__ == '__main__':
    ans = []
    n_val = 2
    k_val = 1
    s = Solution()
    ans = s.combine(n_val, k_val)
    print(ans)
