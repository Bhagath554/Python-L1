def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False
    return True


two = [num for num in range(10, 100) if prime(num)]

print("Two-digit prime numbers:", two)
