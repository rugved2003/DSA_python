l1 = list(map(int,input("List 1:").strip().split()))
l2 = list(map(int,input("List 2:").strip().split()))
n1,n2 = len(l1),len(l2)
s1,s2 = sum(l1),sum(l2)
if n1 == n2 and s1 == s2:
    print("True")
else:
    print("Flase")
