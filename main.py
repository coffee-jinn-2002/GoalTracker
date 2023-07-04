import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class CountdownWindow:
    def __init__(self, target_datetime):
        self.target_datetime = target_datetime
        self.sub_win = tk.Toplevel()
        self.sub_win.geometry("500x100")
        self.sub_win.title("目標カウントダウン")

        self.label_sub = tk.Label(self.sub_win, font=('Helvetica', 48), fg='black')
        self.label_sub.pack()

        self.update_clock()
        self.sub_win.mainloop()

    def update_clock(self):
        dt_now = datetime.now()
        remaining_time = self.target_datetime - dt_now

        if remaining_time.days < 0:
            self.label_sub.configure(text="目標時間を過ぎています")
        else:
            now = str(remaining_time.days) + 'Day ' + str(remaining_time.seconds//3600) + 'h ' + str((remaining_time.seconds//60)%60) + 'm ' + str(remaining_time.seconds%60) + 's '
            self.label_sub.configure(text=now)

        self.sub_win.after(1000, self.update_clock)


class InputWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("目標カウントダウンアプリ")
        self.root.geometry("300x380")

        labels = ["年", "月", "日", "時", "分", "秒"]
        self.entries = []

        tk.Label(self.root,text="【目標時間入力画面】",font=("",16),height=2).pack(fill="x")

        for label in labels:
            frame = tk.Frame(self.root, pady=10)
            frame.pack()
            tk.Label(frame,font=("",14),text=label).pack(side="left")
            entry = tk.Entry(frame,font=("",14),justify="center",width=15)
            entry.pack(side="left")
            self.entries.append(entry)

        tk.Button(self.root,text="開始",font=("",16),width=10,bg="gray",command=self.count).pack()

        self.root.mainloop()

    def count(self):
        try:
            target_year = int(self.entries[0].get())
            target_mon = int(self.entries[1].get())
            target_day = int(self.entries[2].get())
            target_hour = int(self.entries[3].get())
            target_minute = int(self.entries[4].get())
            target_second = int(self.entries[5].get())

            target_datetime = datetime(target_year, target_mon, target_day, target_hour, target_minute, target_second)

            if datetime.now() > target_datetime:
                messagebox.showerror('エラー', '現在時刻より前の日時が入力されています。')
                return

            CountdownWindow(target_datetime)

        except ValueError:
            messagebox.showerror('エラー', '入力された値が不正です。')


if __name__ == "__main__":
    InputWindow()
