n = int(input("Enter number of elements : "))
l = list(map(int,input("Enter the elements:").strip().split()))[:n]
print(l)
p = int(input("postion:"))
new_e = int(input("new element:"))
l.remove(p+1)
l.insert(p,new_e)
print(l)
