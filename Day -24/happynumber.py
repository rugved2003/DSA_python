def sumdigitsquare(n):
    sq =0
    while n != 0:
        digit = n % 10
        sq += digit*digit
        n = n//10

    return sq
def isHappy(n):
    s = set()
    s.add(n)
    while (True):
        if n == 1:
            return True
        n = sumdigitsquare(n)

        if n in s:
            return False
        s.add(n)

    return false;

n = 19
if(isHappy(n)):
    print("yes")
else:
    print("No")