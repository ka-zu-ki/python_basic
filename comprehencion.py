t = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)

r = []
for i in t:
  if i % 2 == 0:
    r.append(i)
print(r)

# 上と同じ
r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
  for j in t2:
    r.append(i * j)
print(r)

# 上と同じ
r = [i * j for i in t for j in t2]
print(r)


w = {'mon', 'tua', 'wed'}
f = {'coffee', 'milk', 'water'}

d = {}
for x, y in zip(w, f):
  d[x] = y
print(d)


# 上と同じ
d = {x: y for x, y in zip(w, f)}
print(d)


s = set()

for i in range(10):
  if i % 2 == 0:
    s.add(i)
print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)


def g():
  for i in range(10):
    yield i

g = g()
print(next(g))

g = (i for i in range(10) if i % 2 == 0)

for x in g:
  print(x)