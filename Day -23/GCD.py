def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(f"GCD of {a} and {b} is {gcd(a, b)}")
