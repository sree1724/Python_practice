# Write a program to count how many times each word appears in a sentence.

sentence = "Write a program to count how many times each word appears in a sentence"

words = sentence.split()

seen = []
for i in words:
   if i not in seen:
       print(i, ':', words.count(i))
       seen.append(i)
       
    