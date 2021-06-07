custom_values = { "name":"Pinto", "default_code":"p001", "default_value":100}
print(custom_values)
data2={}
for k, v in custom_values.items():
    if k.startswith('default_'):

        k=k[8::]
        data2[k]=v
    else:
        data2[k] = v
custom_values=data2
print(custom_values)
