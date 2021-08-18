from typing import List


def possible_word_list(word: str, wordDict: dict) -> List[str]:
    possible_list = []
    for j in range(len(word)):
        letter_ascii = ord(word[j])
        for i in range(97, 123):
            if i != letter_ascii:
                new_word = word[:j] + chr(i) + word[j+1:]
                # print(new_word)
                # possible_string = word.replace(word[j], chr(i))
                possible_string = "".join(new_word)
                # if possible_string in wordListCopy: O(n) -> searching through the array
                if wordDict.get(possible_string) is True:  # O(1)  -> searching for key in Map
                    possible_list.append(possible_string)
    return possible_list


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = dict()
        word_dict = dict()
        for i in wordList:
            word_dict[i] = True
        queue = [(beginWord, 1)]
        visited[beginWord] = True

        if endWord not in wordList:
            return 0
        else:
            while queue:
                currentWord = queue.pop(0)  # currentWord = (HOT,2)
                if currentWord[0] == endWord:
                    return currentWord[1]
                possibleList = possible_word_list(currentWord[0], word_dict)  # pL = [dot, lot]
                for i in possibleList:
                    if not visited.get(i):  # i = dot, lot
                        queue.append((i, currentWord[1] + 1))
                        visited[i] = True
        return 0


if __name__ == '__main__':
    begin = "leet"
    end = "code"
    word_array = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
    # begin = "hit"
    # end = "cog"
    # word_array = ["hot", "dot", "dog", "lot", "log", "cog"]

    s = Solution()
    steps = s.ladderLength(begin, end, word_array)
    print(steps)
