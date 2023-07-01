def isprime(num):
    if num == 1:
        return 0
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return 1
    else:
        return 0

digit = 0
i = 0
prime_sum = 0
rem = 0
check = input("Enter the number: ")
l = len(check)
num = int(check)
while i < l:
    rem = num % 10
    num = (rem * (10 ** (l - 1))) + (num // 10)
    digit = isprime(num)
    prime_sum += digit
    i += 1

if prime_sum == l:
    print("Circular prime")
else:
    print("Non-circular prime")
