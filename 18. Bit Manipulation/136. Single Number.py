class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single = 0
        for num in nums:
            single = single ^ num
            # 0100 xor 0001 = 0101
            # 4 xor 1 = 5
        return single


exampleInputs = [
    [2, 2, 1],
    [4, 1, 2, 1, 2],
    [1],
]

for n in exampleInputs:
    print(Solution().singleNumber(n))
