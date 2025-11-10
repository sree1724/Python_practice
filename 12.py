# Count uppercase and lowercase letters

words = "PyThOn"
upper = 0
lower = 0
for i in words:
    if i.isupper():
        upper += 1
    else:
        lower += 1
print("Upper case",upper)
print("Lower case", lower)