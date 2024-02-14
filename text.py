def rec_fib(n):
    if n > 1:
        return rec_fib(n - 1) + rec_fib(n - 2)
    return n


num = int(input("Digite un numero: "))

for i in range(num):
    print(rec_fib(i))
