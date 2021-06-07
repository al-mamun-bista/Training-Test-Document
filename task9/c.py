data = { 2 : "A", 1 : "BB", 4 : "CC"}
print(data)

data2 = sorted(data.items(),reverse=True)#sorted..but converted into touples
data=dict(data2) #convert touples to dictonarty

print(data)
