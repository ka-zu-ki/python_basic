# import lesson_package.utils
from typing import Reversible
from lesson_package import utils

r = utils.say_twice('hello')

print(r)

ranking = {
  'A': 100,
  'B': 85,
  'C': 95
}

print(sorted(ranking, key=ranking.get, reverse=True))

s = 'sgjkhfsghjkasghfksjhgk'

d = {}
for c in s:
  if c not in d:
    d[c] = 0
  d[c] += 1
print(d)

d = {}
for c in s:
  d.setdefault(c, 0)
  d[c] += 1
print(d)

from collections import defaultdict

d = defaultdict(int)

for c in s:
  d[c] += 1
print(d)

print(d['f'])

from termcolor import colored

print('test')
print(colored('test', 'red'))