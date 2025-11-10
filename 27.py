# remove duplicate characters from a string

string = "programming"
seen = ''
for i in string:
    if i not in seen:
        seen += i
print(seen)