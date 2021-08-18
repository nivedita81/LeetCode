class Solution:
    def romanToInt(self, s: str) -> int:
        if not s or len(s) >= 16:
            return 0
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        total = numerals[s[n-1]]
        for i in range(n-1, 0, -1):
            curr_num = numerals[s[i]]
            prev_num = numerals[s[i-1]]
            if prev_num < curr_num:
                total = total - prev_num
            else:
                total = total + prev_num
        return total


if __name__ == '__main__':
    sol = Solution()
    string = "MCMXCV"
    ans = sol.romanToInt(string)
    print(ans)
