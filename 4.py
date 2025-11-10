# Write a program to check if a string contains only digits.

char = "abhi123sgt456"
digits = "123456"

#result = 0
#result_2 = 0
#
#for i in digits:
#    if i.isdigit():
#        result += 1
#    else:
#        result_2 += 1
#        
#if result == 0:
#    print("the string  contains digits ")
#elif result_2 == 0:
#    print("the string contains characters")
#else:
#    print("the string contains both characters and digits ")

if digits.isdigit():
    print("The string contains only digits ")
else:
    print("the string contaons both string and characters")