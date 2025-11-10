string = "python"
string_2 = "coding"
print("Sorting in Ascending Order", sorted(string))

print(string[::-1])
print(len(string))

descending_order = sorted(string, reverse=True)
print("Sorting in descending Order", descending_order)

print("concatination: ", string + " " + string_2)

print("repeating: ", string_2 *2)

print("Capital letter:", string.upper())
print("Title:", string.capitalize())

print("Palandrome checking:", string ==string[::-1])


word= "madama"
if word == word[::-1]:
    print("\n Yes this is the palandrome")
    
else:
    print("\n No this is not a palandrome")
    
# this is un ordered  count 
#for i in set(word):
#    print(i, ":", word.count(i))
    
    
for i in word:
    print("this is the same:", i, ':', word.count(i))
    
result = ''
for i in word:
    if 'a'<= i <='z':
        result += chr(ord(i) - 32)
    else:
        result += i
    
print("This is the upper case conversion without using .upper() : ", result)


word_2 = 'MADAM'
result_2 = ''
for i in word_2:
    if 'A' <= i <= 'Z':
        result_2 += chr(ord(i) + 32)
    else:
        result_2 += i
print("\n This is the lower case without using .lower(): ", result_2)

count = 0
ovels = ''
for i in word_2:
    if i.lower() in 'aeiou':
        count += 1
        ovels += i
print(count)
print(ovels)        
    
    
    