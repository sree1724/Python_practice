# swap case manually (like .swapcase())

words = "PyThOn"

result = ''

for i in words:
    if i.isupper():
        result += i.lower()
    else:
        result += i.upper()
print(result)