from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(reverse=True)

        res = []
        curr = []
        idx = items[0][0]

        for i, val in items:
            if i == idx:
                if len(curr) < 5:
                    curr.append(val)
            else:
                res.append([idx, sum(curr) // len(curr)])
                curr = [val]
                idx = i

        res.append([idx, sum(curr) // len(curr)])

        res = res[::-1]

        return res


if __name__ == '__main__':
    s = Solution()
    items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
    out = s.highFive(items)
    print(out)

