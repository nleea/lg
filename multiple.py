def multiply(num1: str, num2: str):
    total_sum = 0
    
    if len(num1) == 0 or len(num2) == 0:
        return str(0)
    
    for i, n in enumerate(reversed(num1)):
        n1 = ord(n) - ord("0")
        for x, y in enumerate(reversed(num2)):
            n2 = ord(y) - ord("0")
            total_sum = total_sum + ((n1 * n2) * (10 ** (i + x)))

    return str(total_sum)


print(multiply("123", "456"))
