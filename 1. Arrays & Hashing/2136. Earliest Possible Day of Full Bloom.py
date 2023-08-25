class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        bloom, prevplant = 0, 0
        for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
            bloom = max(bloom, plant + prevplant + grow)
            prevplant += plant
        return bloom


testInputs = [[[1, 4, 3], [2, 3, 1]], [[1, 2, 3, 2], [2, 1, 2, 1]], [[1], [1]]]
for plantTime, growTime in testInputs:
    print(Solution().earliestFullBloom(plantTime, growTime))
