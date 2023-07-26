def isUgly(n):
    if n==1:
        return 1
    if n <= 0:
        return 0

    if n % 2 == 0:
        return (isUgly(n//2))
    if n % 3 == 0:
        return (isUgly(n//3))
    if n% 5 == 0:
        return (isUgly(n//5))

    return 0

no = isUgly(1)

if no == 1:
    print("yes")
else:
    print("No")