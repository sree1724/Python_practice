# convert alternative character to upper

words = "abcd"
result = ''
for i in range(len(words)):
    if i % 2 == 0:
        result += words[i].lower()

    
    else:
        result += words[i].upper()
print(result)