# check if a substring exist in a substring
main_string = "python programming"
substring = "thon"
string = []
for i in range(len(main_string)):
    for j in range(i+1, len(main_string) + 1):
        #dict = string[i] =  j
        dict = main_string[i:j]
        string.append(dict)
for i in string:
    if i != substring:
        #print("yes the given substring is existed in main string ")
        
        continue
    else:
        print(i)
#print("\n", string)
    


        

