def subsets_with_product(a, K):
    result = []
    n = len(a)

    def backtrack(ind, ans, product):
        if product <= K:
            result.append(ans[:])
        if ind == n or product > K:
            return
        for i in range(ind, n):
            ans.append(a[i])
            backtrack(i + 1, ans, product * a[i])
            ans.pop()

    backtrack(0, [], 1)
    return result


# Let's take vector `a` and `K` as sample inputs
a = [17, 18, 6, 11, 2, 4]
K = 100

ans = subsets_with_product(a, K)
for subset in ans:
    print(subset)
