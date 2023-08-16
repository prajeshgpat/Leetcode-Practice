class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n:
            bits += n % 2
            n = n >> 1
        return bits


exampleInputs = [
    0b00000000000000000000000000001011,
    0b00000000000000000000000010000000,
    0b11111111111111111111111111111101,
]
for n in exampleInputs:
    print(Solution().hammingWeight(n))
