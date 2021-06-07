d={}
n = int(input("Enter number of elements : "))
d = [ map(str,input().split()) for x in range(n)]
lst = []

for key,val in d:
    lst.append(key)

lst.sort(reverse=True)

for i in lst:
    for key, val in d:
        if key == i:
            print(key, val)
