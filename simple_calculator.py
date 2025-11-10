# this the simple calculator
print("\n This is the simple calculator \n")
a = int(input("Enter the First number:"))
b = int(input("Enter the second number:"))


choice = int(input("Choose any one option \n \n 1:add \n 2:substact \n 3:muptiplication \n 4:division \n"))

if choice == 1:
    print("\n the adition of two number is :", a +b)
elif choice ==2:
    print(" \nsubstraction of two number is :", a-b)
    
elif choice ==3:
    print(" \n multiplication of two number is :", a*b)
    
elif choice ==4:
    print(" \n substract of two number is :", a//b)
    
else:
    print(" \n Your entered wrong option")    