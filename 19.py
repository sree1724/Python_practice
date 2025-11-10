# remove all space form a string

string = "python is fun"
result = ''
#word = string.split()
#for i in word:
#
#    result += i
#print(result)

for i in string:
    result = string.replace(" ", "")
print(result)