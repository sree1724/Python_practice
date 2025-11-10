# count number of special characters

words = "Hello@2025"
result = 0
for i in words:
    if not i.isalnum():
        result += 1
    
print(result)