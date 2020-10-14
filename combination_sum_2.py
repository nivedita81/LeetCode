from copy import deepcopy
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates = sorted(candidates)
        temp, res = [], []
        if target == 0 or len(candidates) == 0:
            return
        self.dfs(0, 0, target, n, temp, res, candidates)

        res = list(set(tuple(x) for x in res))
        return res

    def dfs(self, index: int, curr_sum: int, target: int, n: int, temp: List[int], res: List[int],
            candidates: List[int]):

        if curr_sum > target:
            return
        if curr_sum == target:
            temp_copy = deepcopy(temp)
            res.append(temp_copy)
            return
        else:
            for i in range(index, n):
                if (curr_sum + candidates[i]) > target:
                    return
                temp.append(candidates[i])
                self.dfs(i + 1, curr_sum + candidates[i], target, n, temp, res, candidates)
                temp.pop()


if __name__ == '__main__':
    ans = []
    array = [10, 1, 2, 7, 6, 1, 5]
    total = 8
    s = Solution()
    ans = s.combinationSum2(array, total)
    print(ans)
