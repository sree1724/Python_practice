# prime numbers

for i in range(9,11):
    if i > 1:
        for num in range(2, int(i ** 0.5) + 1):
            if i % num == 0:
                break
                #seen.append(i)
        else:
            print(i) 
    print("the break is executed")
