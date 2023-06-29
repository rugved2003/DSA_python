def count_repeating_digits(num):
    count = 0
    str_num = str(num)
    
    for i in range(len(str_num)):
        for j in range(i+1,len(str_num)):
            if str_num[i] == str_num[j]:
                count += 1
                break
    if count != 0:
        return "NO"
    else:
        return "YES"

num = int(input())
print(count_repeating_digits(num))
