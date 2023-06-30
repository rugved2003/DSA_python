# def magical_number(n):
#     if n % 9 ==1:
#         print("Magical Number") 
#     else:
#         print("Not a Magical Number")

# n = int(input("Enter the Number to check magical number or not:\n"))
# magical_number(n)

def magical_number(n):
    sum = 0
    while n>0 or sum >9:
        if n == 0:
            n = sum
            sum = 0
        sum += n %10
        n = int(n/10)
    return True if sum == 1 else False
           
            
n = int(input("Enter the number:"))

if(magical_number(n)):
    print("Magical Number")
else:
    print("Not a Magical Number")
