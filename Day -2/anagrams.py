# Anagram program in python
# take user input
String1 = str(input())
String2 = str(input())

String1 = sorted(String1.lower())
String2 = sorted(String2.lower())

print("String1 after sorting: ", String1)
print("String2 after sorting: ", String2)

# check if now strings matches
if String1 == String2:
    print('Strings are anagram')
else:
    print('Strings are not anagram')
