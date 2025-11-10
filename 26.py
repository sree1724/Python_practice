# find the frequency of each word in a sentence
sentence = "to be or not to be"

words = sentence.split()
seen = ''
for i in words:
    if i not in seen:

        print(i, ':', sentence.count(i))
        seen += i