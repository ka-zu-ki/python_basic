l = [1, 3, 4, 5, 5]

# list()で配列作成できる
arr = list('sgnsjkghsjgh')
# print (arr)

# 一つ飛ばし
# print (arr[::2])

# リバース
# print (arr[::-1])

a = [1, 4, 5]
b = [3, 5, 6]
# 配列をネストできる
x = [a, b]
# print (x)

n = [1, 2, 3, 4,  5, 6, 7, 8, 9, 10]

# 後ろに追加
n.append(11)

# 後ろを削除
n.pop()

# 指定したインデックスに追加
n.insert(0, 11)

# 先頭削除
n.pop(0)

# 削除 => すべて消す　破壊的
del n[0]

# 指定した要素を削除
n.remove(10)
# print(n)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

# 配列の結合
print(x + y)
x += y

print(x)

x.extend(y)


r = [1, 2, 3, 4, 5, 1, 2, 3]
# 要素が何番目のインデックスか返す
print(r.index(3))

# 後ろの3が何番目か返す
print(r.index(3, 3))

# もし５が配列に入っていたら
if 5 in r:
    print('exist')

# ソート
r.sort()

# リバース
r.reverse()

# print(r)

s = 'My name is Mike'

# 空白で分割
to_split = s.split(' ')
# print(to_split)

x = ' '.join(to_split)
# print(x)


i = [1, 2, 3, 4, 5]
# 参照渡し
j = i
j[0] = 100
print('j =', j)
print('i =', i)


x = [1, 2, 3, 4, 5]
# 値渡し
y = x.copy()
# y = x[:] => これでもOK
y[0] = 100
print(x)
print(y)
