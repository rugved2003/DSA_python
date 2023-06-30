def print_subsequences(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subsequence = s[i:j]
            if subsequence.isdigit() and int(subsequence) % 11 == 0:
                print(subsequence)

s = input("Enter a string: ")
print_subsequences(s)