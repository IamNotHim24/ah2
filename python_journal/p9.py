def fibonacci(limit,a=0,b=1):
    if a <= limit:
        yield a

        yield from fibonacci(limit,b,a+b)

fib_gen = fibonacci(100)
for fib in fib_gen:
    print(fib,end=' ')
