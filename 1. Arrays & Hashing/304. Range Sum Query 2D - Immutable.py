class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        # calculate prefix sum
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r + 1][c + 1] = (
                    matrix[r][c] + self.dp[r][c + 1] + self.dp[r + 1][c] - self.dp[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )


exampleInputs = [
    [
        [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
    ],
    [2, 1, 4, 3],
    [1, 1, 2, 2],
    [1, 2, 2, 4],
]
obj = NumMatrix(exampleInputs[0][0])
for n in range(1, len(exampleInputs)):
    row1, col1, row2, col2 = exampleInputs[n]
    print(obj.sumRegion(row1, col1, row2, col2))
