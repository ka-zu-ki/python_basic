import random

rand = [random.randint(0, 9) for _ in range(4)]
a = ''
for i in range(len(rand)):
    a += str(rand[i])

print('a = ' + a)

flag = False
numsValidateFlag = False
while flag == False:
    while numsValidateFlag == False:
        b = input('4桁の数字を入力してください -> ')

        if len(b) != 4:
            print("4桁の数値を入力してください!")
        else:
            for i in range(4):
              if (b[i] < "0") or (b[i] > "9"):
                  print("数字ではありません")
                  break

        numsValidateFlag = True

    hit = 0
    for i in range(4):
        if a[i] == b[i]:
            hit = hit + 1
    
    blow = 0
    for i in range(4):
        for j in range(4):
            if (b[0] == a[i]) and (a[i] != b[i]) and (a[0] != b[0]):
                blow = blow + 1

    print('hit' + str(hit))
    print('blow' + str(blow))

    if (hit == 4):
        flag = True
    else:
        numsValidateFlag = False
