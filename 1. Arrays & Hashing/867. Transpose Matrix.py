class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transpose = []
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            transpose.append(row)

        return transpose


exampleInputs = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6]]]
for n in exampleInputs:
    print(Solution().transpose(n))
