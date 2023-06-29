arr = int(input("Enter Number: "))
s= str(arr)
even,odd = 0,0

for i in range(len(s)):
    if i % 2 == 0:
        even += int(s[i])
    else:
        odd += int(s[i])

print(odd-even)


####  FOR ARRAY ###

"""
s = list(map(int,input().split()))
even,odd = 0,0

for i in range(len(s)):
    if i % 2 == 0:
        even += int(s[i])
    else:
        odd += int(s[i])

print(odd-even)
"""
    


    

