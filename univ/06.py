total = 0
a = 1

while total <= 50:
    print("処理回数" + str(a) + " 変数totalの値:" + str(total) + " 変数aの値" + str(a))
    total += a
    a += 1

print("total =" + str(total))

result = 0
b = 1

while result <= 101:
    if b % 2 != 0:
        result += b
    b += 1

print("total =" + str(result))
