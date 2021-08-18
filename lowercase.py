# a - 97, z - 122
# A - 65,  Z - 90
# '0' - 48, '9' - 57


class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ""
        for idx, i in enumerate(str):
            # print(int(i))
            # if 65 <= ord(i) <= 90
            if ord("A") <= ord(i) <= ord("Z"):
                result = result + chr(ord(i) + 32)
            else:
                result = result + i
        return result


if __name__ == '__main__':
    ans = Solution()
    name = "NIVEdita"
    lower_case = ans.toLowerCase(name)
    print(lower_case)
