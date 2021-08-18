class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count, sum_val = 0, 0
        for i in columnTitle[::-1]:
            sum_val = sum_val + (26 ** count) * (ord(i) - 64)
            count = count + 1

        return sum_val


# a - 97, z - 122
# A - 65,  Z - 90
# '0' - 48, '9' - 57
# ord('Z') gives 90, but ord('Z') - 64 gives order in original alphabet set --> 26
# ord('Z')

if __name__ == '__main__':
    string = "A"
    ans = Solution().titleToNumber(string)
    print(ans)
