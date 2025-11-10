# reverse words in a sentence

sentence = "python is fun"

words = sentence.split()
reverse = words[::-1]
reverse_final = " ".join(reverse)
#print(words, reversed= True)
print(reverse_final)