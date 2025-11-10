string = "success"

seen = ''
freq_dist = {}

for i in string:
    if i not in seen:
        freq = string.count(i)
        
        dist_freq = freq_dist[i] = freq
        seen += i

sorted_freq = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)

for chr, val in sorted_freq:
    print(f"{chr} : {val}")

if len(sorted_freq) >= 2:
    
    character = sorted_freq[1][0]
    value = sorted_freq[1][1]
    print(f"the highest frequency is : {character} : {value} ")
else:
    print("there is no enough value for second highest")