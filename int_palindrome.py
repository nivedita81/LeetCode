class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        sum = 0
        num = x

        while num != 0:
            sum = (sum * 10) + (num % 10)
            num = num // 10

        if sum == x:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    input_val = 121
    print(s.isPalindrome(input_val))
