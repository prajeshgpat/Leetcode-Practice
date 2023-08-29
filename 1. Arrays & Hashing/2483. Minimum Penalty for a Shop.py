class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = 0
        index = 0
        for open in [*customers]:
            if open == "N":
                penalty += 1
                return index
            index += 1
        return index


testInputs = [
    "YYNY",  # 2
    "NNNNN",  # 0
    "YYYY",  # 4
]
for string in testInputs:
    print(Solution().bestClosingTime(string))
