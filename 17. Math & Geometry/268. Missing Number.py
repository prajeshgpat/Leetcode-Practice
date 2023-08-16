class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        length = len(nums)
        gaussSum = (length * (length + 1)) // 2  # Calculates arithmetic
        listSum = sum(nums)
        return gaussSum - listSum


exampleInputs = [
    [3, 0, 1],
    [0, 1],
    [9, 6, 4, 2, 3, 5, 7, 0, 1],
]
for n in exampleInputs:
    print(Solution().missingNumber(n))
