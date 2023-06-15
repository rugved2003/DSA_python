'''def reverse(arr):
    a = arr[::-1]
    return a
arr = [10,45,678,3325,78]
print("reversed array :",reverse(arr))
'''

def reverselist(A,start,end):
    while start < end:
        A[start],A[end] = A[end], A[start]
        start +=1
        end -=1


A = [1, 2, 3, 4, 5, 6]
print(A)
reverselist(A, 0, 5)
print("Reversed list is")
print(A)