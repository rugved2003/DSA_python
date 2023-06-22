def findpairs(a1,a2,x):
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i] + a2[j] == x:
                print(a1[i],a2[j])
a1 = list(map(int,input("Array 1:").split()))
a2 = list(map(int,input("Array 2:").split()))
x = int(input("sum:"))
findpairs(a1, a2, x)
