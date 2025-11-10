# find the longest word

sentence = " find the longest word"
words = sentence.split()
result = ''
for i in words:
    if len(i) >= len(result):
        result = i
    
print(result)

