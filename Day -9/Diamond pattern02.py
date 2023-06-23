n = int(input())
for i in range(n):
    for j in range(2*n-1):
        if(i+j<n-1 or i+j >= n+2*i):
            print(" ",end = "")
        else:
            print(i+1,end = "")
    print()
    
for i in range(n-1):
    for j in range(2*n-1):
        if(i+j<= 2*i or i+j>=(2*n-2)):
            print(" ",end = "")
        else:
            print(n-1-i,end = "")
    print()
