class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        pairs = set()
        for i in range(len(s) - k + 1):  # [00]110110 0[01]10110 ... 001101[10]
            pairs.add(s[i : i + k])
        return len(pairs) == 2**k  # 2^k


exampleInputs = [("00110110", 2), ("0110", 1), ("0110", 2)]
for s, k in exampleInputs:
    print(Solution().hasAllCodes(s, k))
