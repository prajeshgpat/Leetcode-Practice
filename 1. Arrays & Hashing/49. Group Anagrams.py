from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagram_groups = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_groups[sorted_word].append(word)
        result = list(anagram_groups.values())

        return result


testInputs = [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"]]
for strs in testInputs:
    print(Solution().groupAnagrams(strs))
