# Write a program to find the second most frequent character in a string

word = "aabbbcccc"
freq_dict = {}
seen = ''

for i in word:
    if i not in seen:
        freq = word.count(i)
        dict_freq = freq_dict[i] = freq
        seen += i

sort_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

for chr, val in sort_freq:
    print(f"{chr} : {val}")

if len(sort_freq) >= 2:
    char_freq = sort_freq[1][0]
    val_freq = sort_freq[1][1]
    print(f"the second most frequent character in the string is: {char_freq} and it is repeated in {val_freq} Times")

else:
    print("minum two string requires to print the second most frequency nuber")
   