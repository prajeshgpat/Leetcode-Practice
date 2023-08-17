class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i, j = 0, 0  # Pointers for s and t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move pointer for s
            j += 1  # Always move pointer for t

        return i == len(s)


exampleInputs = [("abc", "ahbgdc"), ("axc", "ahbgdc")]
for s, t in exampleInputs:
    print(Solution().isSubsequence(s, t))
