import math

num = 1
name = '1'

# print(num, type(num))
# print(name, type(name))

new_num = int(name)

# print(new_num)

# print('Hi', 'Mike')

#sep => セパレイトの略　分割できる
# print('Hi', 'Mike', sep=',', end='\n')

result = math.sqrt(25)
# print (result)

#乗算
# 3 ** 3 => 27

# help関数 => ドキュメント
# print (help(math))

# \nで改行

#""を３つで囲むと改行
#\で次の行からプログラムを開始する
# print ("""\
  # line1
  # line2
  # line3
  # line3
  # line3\
# """)


word = 'Ptyhon is Good'

# -1で最後のインデックス
# print (word[-1])

# slice => 0:2
# print (word[0:2])
# 最初の2つ
# print (word[:2])
# 最初の2つ以外
# print (word[2:])
# 文字数
# print (len(word))

# find関数
# print (word.find('t'))

# print (word.count('t'))

# 先頭以外を小文字にする
# print (word.capitalize())

# 単語の先頭を大文字にする
# print (word.title())

# すべて大文字にする
# print (word.upper())

# すべて小文字にする
# print (word.lower())

# 置き換え
# print (word.replace('t', 'k'))


a = 'a'
# 先頭にfで文字列に代入できる
# print (f'a is {a}')

# strで型を文字列に変換
# print (type(str(1)))

