# Write a program to find the frequency of a particular character.
string = "abhishek"
char = "a"   # character whose frequency we want to find
count = 0

for i in string:
    if i == char:
        count += 1

print("The frequency of", char, "is:", count)
