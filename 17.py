# Replace all vowels with '*'

words = "hello world"
result = ''
for i in words:
    if i.lower() in 'aeiou':
        result += i.replace("i", "*")
        
    else:
        result += i
print(result)