class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        steps = 0
        while num > 1:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps + 1


exampleInputs = [
    14,
    8,
    123,
]
for num in exampleInputs:
    print(Solution().numberOfSteps(num))
