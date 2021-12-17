import random
import tkinter as tk
import tkinter.messagebox as tmsg

a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]


def button_click():
    text = editbox1.get()

    isok = False
    if len(text) != 4:
        tmsg.showerror("エラー", "4 桁の数字を入力してください")
    else:
        kazuok = True
        for i in range(4):
            if (text[i] < "0") or (text[i] > "9"):
                tmsg.showerror("エラー", "数字ではありません")
                kazuok = False
                break
    if kazuok:
        isok = True
    if isok:
        # 4 桁の数字であったとき
        # ヒットを判定
        hit = 0
        for i in range(4):
            if a[i] == int(text[i]):
                hit = hit + 1
        # ブローを判定
        blow = 0
        for j in range(4):
            for i in range(4):
                if (int(text[j]) == a[i]) and (a[i] != int(text[i])) and (a[j] != int(text[j])):
                    blow = blow + 1
                    break

    # ヒットが 4 なら当たりで終了
    if hit == 4:
        tmsg.showinfo("当たり", "おめでとうございます。当たりです")
        # プログラム終了（新たに追加した部分）
        root.destroy()
    else:
        # ヒット数とブロー数を表示
        history_box.insert(tk.END, text + " ／H:" +
                           str(hit) + " B:" + str(blow) + "\n")
        editbox1.delete(0, tk.END)


root = tk.Tk()
root.geometry('600x400')
root.title('数当てゲーム')

history_box = tk.Text(root, font=('Healvetica', 14))
history_box.place(x=400, y=0, width=200, height=400)

label1 = tk.Label(root, text='数を入力してね', font=('Healvetica', 14))
label1.place(x=20, y=20)

editbox1 = tk.Entry(width=4, font=('Healvetica', 28))
editbox1.place(x=120, y=60)

button1 = tk.Button(root, text='チェック', font=(
    'Healvetica', 14), command=button_click)
button1.place(x=220, y=60)

root.mainloop()
