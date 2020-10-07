from copy import deepcopy
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates = sorted(candidates)
        temp, res = [], []
        if target == 0 or len(candidates) == 0:
            return
        self.dfs(0, 0, target, n, temp, res, candidates)
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
                self.dfs(i, curr_sum + candidates[i], target, n, temp, res, candidates)
                temp.pop()


if __name__ == '__main__':
    ans = []
    array = [8, 7, 4, 3]
    total = 11
    s = Solution()
    ans = s.combinationSum(array, total)
    print(ans)
