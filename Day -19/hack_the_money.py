def solve(N, arr):
    if arr == N:
        return True
    if arr > N:
        return False
    
    return solve(N, arr * 10) or solve(N, arr * 20)

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print("Yes")
    else:
        if solve(n, 1):
            print("Yes")
        else:
            print("No")
