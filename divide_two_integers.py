class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 0

        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1

        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        while dividend >= divisor:
            current_divisor, multiple = divisor, 1
            while dividend >= (current_divisor * 2):
                current_divisor *= 2
                multiple *= 2

            dividend -= current_divisor
            result += multiple

        return result * sign


s = Solution()
print(s.divide(-1, 1))
