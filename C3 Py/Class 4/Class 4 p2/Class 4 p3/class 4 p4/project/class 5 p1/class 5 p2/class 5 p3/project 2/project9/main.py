

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_series(n):
    return [fibonacci(i) for i in range(n)]


num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

print(fibonacci_series(num_terms))

