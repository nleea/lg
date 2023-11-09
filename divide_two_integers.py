class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0 or dividend == 0:
            return 0

        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        if divisor > 0 and (dividend - divisor) - 1 > divisor:
            return self.divide(dividend - divisor, divisor)
        elif divisor < 0 and (dividend - (-1 * divisor)) - 1 > divisor:
            return self.divide(dividend - (-1 * divisor), divisor)

        if divisor > 0:
            return (dividend - divisor) - 1
        else:
            return dividend + 1


s = Solution()
print(s.divide(7, -3))
