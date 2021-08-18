class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # max_len = max(len(a), len(b))
        #
        # a = a.zfill(max_len)
        # b = b.zfill(max_len)
        #
        # result = ""
        # carry = 0
        #
        # for i in range(max_len - 1, -1, -1):
        #     r = carry
        #     r = r+1 if a[i] == '1' else 0
        #     r = r+1 if b[i] == '1' else 0
        #     result = ('1' if r % 2 == 1 else '0') + result
        #     carry = 0 if r < 2 else 1
        #
        # if carry != 0:
        #     result = '1' + result
        #
        # return result
        len_a = len(a) - 1
        len_b = len(b) - 1
        carry = 0
        result = ""

        while len_a >= 0 or len_b >= 0 or carry:
            one = ord(a[len_a]) - ord('0') if len_a >= 0 else 0
            two = ord(b[len_b]) - ord('0') if len_b >= 0 else 0

            sum = one + two + carry
            val = chr(sum % 2 + ord('0'))
            result = "".join(val + result)

            carry = sum // 2

            len_a = len_a - 1
            len_b = len_b - 1

        return result


if __name__ == '__main__':
    str_a = '11'
    str_b = '1'
    s = Solution()
    output = s.addBinary(str_a, str_b)
    print(output)
