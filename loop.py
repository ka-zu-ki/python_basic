count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')


some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

for i in some_list:
    print(i)


# range
for _ in range(10):
    print('hello')

#5~10
for i in range(5, 10):
  print(i)

print('#############################')

for i in range(2, 10, 3):
# ３個ずつ
  print(i)


# enumerate
for i, fruit in enumerate(['apple', 'banana', 'orange']):
  print(i, fruit)


# zip
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
  print(day, fruit, drink)


# dict.items()
d = {'x': 100, 'y': 200}
for k, v in d.items():
  print(k, ':', v)


