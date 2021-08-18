# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace
# and initial word order.


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        result = ""

        for i in s:
            if ord(i) == 32:
                arr.reverse()
                result = result + "".join(arr)
                # result = "".join(result + " ")
                arr.clear()
                result = "".join(result + " ")
            else:
                arr.append(i)

        arr.reverse()
        result = result + "".join(arr)

        return result


if __name__ == '__main__':
    sol = Solution()
    input_str = "Let's take LeetCode contest"

    reversed_word = sol.reverseWords(input_str)
    print(reversed_word)
