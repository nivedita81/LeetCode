import sys


class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapVal = dict()

        for index, val in enumerate(s):
            if val in mapVal:
                mapVal[val] = -1
            else:
                mapVal[val] = index

        # minimum = -sys.maxsize - 1

        for i in mapVal:
            # print(mapVal[i])
            if mapVal[i] > -1:
                # minimum = mapVal[i]
                return mapVal[i]
        return -1


if __name__ == '__main__':
    string = "loveleetcode"
    s = Solution()
    index = s.firstUniqChar(string)
    print(index)

