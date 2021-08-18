def get_alphabet(input_str: str) -> str:
    map_value = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h",
                 "9": "i", "10#": "j", "11#": "k", "12#": "l", "13#": "m", "14#": "n",
                 "15#": "o", "16#": "p", "17#": "q", "18#": "r", "19#": "s", "20#": "t",
                 "21#": "u", "22#": "v", "23#": "w", "24#": "x", "25#": "y", "26#": "z"
                 }
    return map_value[input_str]


class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypt_val = ""
        for i in range(len(s) - 1, 0):
            if s[i] == "#":
                result = ""
                ans = ""
                j = i - 1
                k = i - 2
                result = "".join(result + s[k] + s[j] + s[i])
                ans = get_alphabet(result)
                decrypt_val = "".join(decrypt_val + ans)
                i - 3
                del ans
                del result
            else:
                result = ""
                ans = ""
                result = "".join(result + s[i])
                ans = get_alphabet(result)
                decrypt_val = "".join(decrypt_val + ans)
                i - 1
                del ans
                del result
        return decrypt_val[::-1]


if __name__ == '__main__':
    s = Solution()
    input_val = "10#11#12"
    output = s.freqAlphabets(input_val)
    print(output)
