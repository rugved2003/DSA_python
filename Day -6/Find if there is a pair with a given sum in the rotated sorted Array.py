def pairinarray(arr,n,x):
    for i in range(0,n-1):
        if (arr[i] > arr[i + 1]):
            break
    l = (i + 1) % n
    r = i
    
    while(l !=  r):
        if(arr[l]+arr[r] == x):
            return True
        if(arr[l] + arr[r] < x):
            l = (l+1)%n
        else:
            r = (n +r -1) % n
    return False
    
arr = [11,15,6,8,9,10]
X = 26
N = len(arr)
if(pairinarray(arr,N,X)):
    print("true")
else:
    print("false")
