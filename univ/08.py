year = int(input("今年は西暦何年ですか:"))
name = input("あなたのお名前を入力してください:")
birth = int(input("生まれた年を入力してください:"))

print(name + "さんの年齢は" + str(year - birth) + "です")

while True:
    year2 = int(input("今年は西暦何年ですか:"))
    if year2 == 9999:
        print("処理を終了しました")
        break
    name2 = input("あなたのお名前を入力してください:")
    birth2 = int(input("生まれた年を入力してください:"))
    print(name2 + "さんの年齢は" + str(year2 - birth2) + "です")
