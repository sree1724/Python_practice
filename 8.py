# Write a program to count how many words are there in a sentence.

sentence = "Write a program to count how many words are there in a sentence"

word = sentence.split()
count = 0
for i in word:
    count += 1
print(count)