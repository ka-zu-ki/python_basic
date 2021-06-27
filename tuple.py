t = (1, 2, 3, 4, 5)

# 代入以外のlistの操作ができる => immutable
# ,で区切るとtuple

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

# 入れ替え
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)


