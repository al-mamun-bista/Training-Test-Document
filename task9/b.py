first_list = [20, 39, 34, 20, 24, 20, 10, 11]

print(first_list)
frequency = {}
for item in first_list:
    if (item in frequency):
        frequency[item] += 1
    else:
        frequency[item] = 1
#print(freq)
for k,v in frequency.items():
    print(k,end=" ")
