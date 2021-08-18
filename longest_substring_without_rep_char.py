class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visited = [-1] * 256
        curr_len = 1
        max_len = 0
        if s is None or len(s) == 0:
            return 0

        visited[ord(s[0])] = 0

        for i in range(1, len(s)):
            prev_index = visited[ord(s[i])]
            if prev_index == -1 or (i - curr_len > prev_index):
                curr_len += 1
            else:
                if curr_len > max_len:
                    max_len = curr_len

                curr_len = i - prev_index
            visited[ord(s[i])] = i

        if curr_len > max_len:
            max_len = curr_len

        return max_len


if __name__ == '__main__':
    string = "abcdcefbc"
    ans = Solution().lengthOfLongestSubstring(string)
    print(ans)
