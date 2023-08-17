class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = abs(dividend)
        d = abs(divisor)
        q = 0

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        while (n - d) >= 0:
            i = 0
            while n - (d << i << 1) >= 0:
                i += 1
            q += 1 << i
            n -= d << i

        if (dividend > 0) == (divisor > 0):
            return q
        else:
            return -q


exampleInputs = [(10, 3), (7, -3)]
for dividend, divisor in exampleInputs:
    print(Solution().divide(dividend, divisor))
