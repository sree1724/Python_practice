# Write a program to remove duplicate characters from a string.

words = "abhiabhishekshek"
#seen = []
#fd=""
#for i in words:
#    if i not in seen:
#        seen.append(i)
#print(seen)


seen = ''

for i in words:
    if i not in seen:
        seen += i
print(seen)