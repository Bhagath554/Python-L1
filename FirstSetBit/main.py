def first(n):
    count = 1
    while n:
        if n & 1:
            break
        count += 1
        n >>= 1
    return count

num = int(input("Enter the number: "))
print(first(num))
