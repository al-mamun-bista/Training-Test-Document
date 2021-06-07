dic = { "name":"Pinto", "default_code":"p001", "default_value":100}
d={}
for key, val in dic.items():
    if key.startswith('default_'):

        key=key[8::]
        d[key]=val
    else:
        d[key] = val
print(d)