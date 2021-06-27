# 重複を省く
s = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 3, 2, 8}

print(s & s2)
print(s | s2)
print(s ^ s2)

s.add(7)
print(s)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)