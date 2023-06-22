def Minstep(a,n):
    pos = 0
    neg = 0
    zero = 0
    
    step = 0
    
    for i in range(n):
        if a[i] == 0:
            zero += 1
            
        elif a[i]<0:
            neg += 1
            step = step + (-1-a[i])
            
        else:
            pos +=1
            step = step + (a[i] - 1)
            
    if neg % 2 == 0:
        step = step +zero
    else:
        if zero >0:
            step = step +zero
        else:
            step = step +2
    return step 
    
a = list(map(int,input("Enter the array:").split()))
n = len(a)
print(Minstep(a,n))
