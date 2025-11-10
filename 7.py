# Write a program to capitalize the first letter of every word in a sentence (without using .title()).

words = "Write a program to capitalize the first letter of every word in a sentence"

word = words.split()
result=''
for i in word:
    first = i[0].upper()
    rest = i[1:]
    
    result += first + rest + ' '
print(result)
    