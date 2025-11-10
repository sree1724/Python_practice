n = int(input("enter the years: "))

jan = 31
feb = 0
mar =31
apr = 30
may =31
jun =30
jul= 31
aug =31
sep = 30
oct =31
nev =30
dec =31
if n % 4 ==0 and n % 100 != 0 or n % 400 == 0:
    print("this is leap yera ")
    feb += 29

    

else:
    print("this is not a leap years")
    feb += 28



