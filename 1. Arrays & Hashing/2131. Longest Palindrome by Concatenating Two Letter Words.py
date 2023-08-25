from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        pal, middle = 0, 0
        bank = defaultdict(lambda: 0)

        for word in words:
            bank[word] += 1

        for word in list(bank):
            if word == word[::-1]:
                if bank[word] % 2 == 1:
                    middle = 2
                pal += (bank[word] // 2) * 4
            elif bank[word[::-1]] > 0:
                pal += min(bank[word], bank[word[::-1]]) * 4
                bank[word] = 0
        return max(pal + middle, 0)


testInputs = [
    ["lc", "cl", "gg"],
    ["ab", "ty", "yt", "lc", "cl", "ab"],
    ["cc", "ll", "xx"],
]
for words in testInputs:
    print(Solution().longestPalindrome(words))
