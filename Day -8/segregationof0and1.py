def segregate0and1(arr):
    n = len(arr)
    count = 0
    
    for i in range(n):
        if arr[i] == 0:
            count += 1
            
    for i in range(count):
        arr[i] = 0
    for i in range(count,n):
        arr[i] = 1

def print_arr(arr):
    print("Array after segregation is ",end = " ")
    for i in range(len(arr)):
        print(arr[i],end = ' ')

arr = list(map(int,input("Enter the array: ").split()))
segregate0and1(arr)
print_arr(arr)
