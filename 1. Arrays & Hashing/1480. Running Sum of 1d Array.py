class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


exampleInputs = [[1, 2, 3, 4], [1, 1, 1, 1, 1], [3, 1, 2, 10, 1]]
for n in exampleInputs:
    print(Solution().runningSum(n))
