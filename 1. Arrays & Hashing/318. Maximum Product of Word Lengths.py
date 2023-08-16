class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        hashset = []
        for word in words:
            hashset.append(set(word))

        max_val = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if not (hashset[i] & hashset[j]):
                    max_val = max(max_val, len(words[i]) * len(words[j]))
        return max_val


exampleInputs = [
    ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],
    ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],
    ["a", "aa", "aaa", "aaaa"],
]
for n in exampleInputs:
    print(Solution().maxProduct(n))
