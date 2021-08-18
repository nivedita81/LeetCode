class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        dp[0], dp[2] = 0, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    a = Solution()
    stepsCount = a.climbStairs(3)
    print(stepsCount)

