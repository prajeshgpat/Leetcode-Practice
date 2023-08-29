class Solution:
    def bestClosingTime(self, customers: str) -> int:
        score = 0
        bestScore = 0
        closingTime = -1
        for hour in range(len(customers)):
            if customers[hour] == "Y":
                score += 1
            else:
                score -= 1

            if score > bestScore:
                bestScore = score
                closingTime = hour
        return closingTime + 1


testInputs = ["YYNY", "NNNNN", "YYYY", "YNYY"]  # 2  # 0  # 4  # 4
for string in testInputs:
    print(Solution().bestClosingTime(string))
