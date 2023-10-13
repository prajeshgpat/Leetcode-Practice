# Pascal's triangle python 3 code
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = [[1]]
        for row in range(1, numRows):
            prevRow = pascal[-1]
            currRow = [1]
            for i in range(1, row):
                currRow.append(prevRow[i - 1] + prevRow[i])

            currRow.append(1)
            pascal.append(currRow)

        return pascal


testInputs = [
    5,
    1,
    10,
]
for numRows in testInputs:
    print(Solution().generate(numRows))
