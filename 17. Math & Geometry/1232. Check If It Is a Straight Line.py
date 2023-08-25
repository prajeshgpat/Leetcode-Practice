class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[0]
            x2, y2 = coordinates[1]
            x, y = coordinates[i]
            if (y2 - y1) * (x - x1) != (y - y1) * (x2 - x1):
                return False
        return True


testInputs = [
    [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],
    [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]],
]
for coordinates in testInputs:
    print(Solution().checkStraightLine(coordinates))
