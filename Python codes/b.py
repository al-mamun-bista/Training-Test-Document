list1 = [20, 39, 34, 20, 24, 20, 10, 11]

print("sorted llist", list1.sort())
res = []
for i in list1:
    if i not in res:
        res.append(i)


print(res)



