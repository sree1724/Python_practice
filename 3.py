# Write a program to swap case (uppercase → lowercase and vice versa).

words = 'PyThOn'
result = ''
for i in words:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
    else:
        result += i
print(result)
        