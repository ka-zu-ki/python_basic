d = {'a': 1, 'b': 2}

print(d.keys())
print(d.values())

d2 = {'a': 10, 'c': 30}

d.update(d2)
print(d)

print(d['a'])
print(d.get('a'))

print('a' in d)

d.clear()
print(d)

# 参照渡し
v = {'a': 1}
b = v
b['a'] = 100
print(v)
print(b)

# 値渡し
x = {'a': 1}
y = x.copy()
y['a'] = 100
print(x)
print(y)