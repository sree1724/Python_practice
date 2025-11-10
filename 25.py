# conut digits, alphabets, and symbols

words = "Hello123!"

alphabets = 0
digits = 0
symbols = 0
for i in words:

    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        digits += 1
    else:
        symbols += 1
print(f"alphabets: {alphabets}  \ndigits: {digits} \nsymbols:{symbols}")