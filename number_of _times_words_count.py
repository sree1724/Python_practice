words = 'aeiuondshsnsiwk'
count = 0
result = []
for i in words:
    if i.lower() in 'aeiou':
        count += 1
        result.append(i)
        print(i, ':', words.count(i))
print(count)
print(result)        