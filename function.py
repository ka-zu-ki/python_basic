def say_something(*args):
  for arg in args:
    print(arg)

  print(args)

say_something('hi!', 'Mike', 'Nancy')

t = ('Mike', 'Nancy')
say_something('Hi!', *t)

d = {
  'entree': 'beef',
  'drink': 'ice coffee',
  'desert': 'ice'
}

def menu(kwargs):
  for k, v in kwargs.items():
    print(k, v)

menu(d)

# クロージャー
def circle_area_func(pi):
  def circle_area(radius):
    return pi * radius * radius

  return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))


# デコレーター
def print_info(func):
  def wrapper(*args, **kwargs):
    print('start')
    result = func(*args, **kwargs)
    print('end')
    return result
  return wrapper

@print_info
def add_num(a, b):
  return a + b

r = add_num(10, 20)
print(r)


@print_info
def sub_num(a, b):
  return a - b

r = sub_num(20, 10)
print(r)

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
  for word in words:
    print(func(word))

# def sample_func(word):
#   return word.capitalize()

# ラムダ関数
sample_func = lambda word: word.capitalize()

change_words(l, sample_func)

# 単純なループ
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
  print(i)

print('----------------------------------------')

# ジェネレーター => 他の処理を挟める
def greeting():
  yield 'Good morning'
  yield 'Good afternoon'
  yield 'Good night'

g = greeting()

# nextで実行する
print(next(g))

print('aaaaaaaaaa')

print(next(g))

print('aaaaaaaaaa')

print(next(g))

