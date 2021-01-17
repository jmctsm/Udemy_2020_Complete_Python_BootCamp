print({x:x**2 for x in range(10)})

d = {'k1': 1, 'k2': 2}
for k in d.keys():
    print(k)
for v in d.values():
    print(v)
for item in d.items():
    print(item)

key_view = d.keys()
print(key_view)

d['k3'] = 3
print(d)

print(key_view)