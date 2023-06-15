def getminmax(arr):
    arr.sort()
    minmax = {'min': arr[0], "max": arr[-1]}
    return minmax

arr = [100,45,74,23,10,98]
minmax = getminmax(arr)
print("Minmim element is",minmax['min'])
print("Maximum element is",minmax['max'])