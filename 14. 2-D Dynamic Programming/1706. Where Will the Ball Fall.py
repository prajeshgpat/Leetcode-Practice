class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        rows = len(grid)
        cols = len(grid[0])
        answer = [0] * len(grid[0])

        for col in range(cols):
            newcol, tmpcol = col, col
            for row in range(rows):
                newcol += grid[row][newcol]
                if (
                    newcol == -1
                    or newcol == cols
                    or grid[row][newcol] != grid[row][tmpcol]
                ):
                    newcol = -1
                    break
                tmpcol = newcol
            answer[col] = newcol
        return answer


testInputs = [
    [
        [1, 1, 1, -1, -1],
        [1, 1, 1, -1, -1],
        [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, -1, -1, -1],
    ],
    [[-1]],
    [
        [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1],
        [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1],
    ],
]
for grid in testInputs:
    print(Solution().findBall(grid))
