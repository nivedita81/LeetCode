from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        count = 1

        for j in range(1, len(chars) + 1):
            if j < len(chars) and chars[j] == chars[j - 1]:
                count = count + 1
            else:
                chars[i] = chars[j - 1]
                i = i + 1

                if count > 1:
                    for k in str(count):
                        chars[i] = k
                        i = i + 1
                count = 1

        chars = chars[:i]

        return i


if __name__ == '__main__':
    arr = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    val = Solution().compress(arr)
    print(val)
