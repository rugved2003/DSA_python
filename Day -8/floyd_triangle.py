def floyd(n):
    c= 0
    for i in range(n+1):
        for j in range(i):
            c += 1
            print(c,end = " ")
        print()
        
n=int(input("Enter the number of rows: "))
floyd(n)
