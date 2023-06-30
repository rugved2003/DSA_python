def contains_only_digits(number,digits):
    for digit in str(number):
        if digit not in digits:
            return False
    return True

def count_of_digits(m,n,digits):
    count = 0
    for number in range(m,n+1):
        if contains_only_digits(number,digits):
            count += 1
    return count

m = int(input("Enter lower bound number: "))
n = int(input("Enter higher bound number: "))
digits = ['1','4','9']

print(count_of_digits(m,n,digits))
