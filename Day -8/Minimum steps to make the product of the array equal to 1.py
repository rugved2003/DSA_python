def Minstep(a):
    pos,neg,zero,step = 0,0,0,0
    for i in range(len(a)):
        if a[i] == 0:
            zero += 1
        elif a[i] < 0:
            neg += 1
            step  = step +(-1 -a[i])
        else:
            pos += 1
            step = step + (a[i]-1)
    if neg % 2 == 0:
        step = step+zero
    else:
        if zero > 0:
           step = step + zero
        else:
            step = step +2
    return step
a = list(map(int,input("Enter the array:").split()))
print(Minstep(a))
