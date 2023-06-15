print("Enter the String: ")
s = str(input())
n = []
for i in s:
    if i.isdigit():
        n.append(int(i))
 
print("The numbers list is:", n)


