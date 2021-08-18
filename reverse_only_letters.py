# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
# and all letters reverse their positions.


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        str_list = list(S)
        front, back = 0, len(str_list) - 1
        while front < back:
            flag = 0
            if (65 <= ord(str_list[front]) <= 90 or 97 <= ord(str_list[front]) <= 122) and (
                    65 <= ord(str_list[back]) <= 90 or 97 <= ord(str_list[back]) <= 122):
                str_list[front], str_list[back] = str_list[back], str_list[front]
                front = front + 1
                back = back - 1
                flag = 1

            if not flag:
                if not (65 <= ord(str_list[front]) <= 90 or 97 <= ord(str_list[front]) <= 122):
                    front = front + 1
                else:
                    back = back - 1

        result = "".join(str_list)

        return result


if __name__ == '__main__':
    s = Solution()
    # input_str = "ab-cd"
    # input_str = "a-bC-dEf-ghIj"
    input_str = "Test1ng-Leet=code-Q!"
    output_str = s.reverseOnlyLetters(input_str)
    print(output_str)
