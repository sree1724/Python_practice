# replace all vowels with *
string = "hellow world"
vowels = "AEIOUaeiou"
count = ''
for i in string:
    if i in vowels:
        count += "*"
    else:
        count += i
print(count)