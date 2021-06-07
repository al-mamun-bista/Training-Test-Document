dic1 = { 2 : "AA", 1 : "BB", 4 : "CC"}
print(dic1)

aa = sorted(dic1.items(),reverse=True)
bb = dict(aa)

print(bb)
