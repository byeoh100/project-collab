def factorial(num):
    if num == 0:
        return 1
    prod = 1
    while num > 0:
        prod *= num
        num -= 1
    return prod

print(factorial(4))