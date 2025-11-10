# Count how many times a character appears

words = "banana"
seen= []
for i in words:
    if i not in seen:
        seen.append(i)
        print(i, ':', words.count(i))