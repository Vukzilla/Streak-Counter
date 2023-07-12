from tkinter import *

app = Tk()

width = 250
height = 200

app.title("Streak")
app.geometry("250x200")
app.resizable(False, False)

font_size = 12
custom_font = ("Arial", font_size)

def update_file():
    with open("Streak.txt", "w") as file:
        file.write(f"Streak - {streak}\n")
        file.write(f"Highscore - {highscore}")

def add():
    global streak, highscore
    streak += 1
    print("Streak:", streak)
    if streak > highscore:
        highscore = streak
        print("Highscore:", highscore)
    update_file()
    text = Label(app, text=streak, font=custom_font)
    text.place(x=width/2 - 5, y=50)

def reFresh():
    global streak
    streak = 0
    update_file()
    text = Label(app, text=streak, font=custom_font)
    text.place(x=width/2 - 5, y=50)
    

addStreak = Button(text="Streak +1", width=16, command=add)
addStreak.place(x=width/2 - 60, y=110)

reStreak = Button(text="Reset Streak", width=10, command=reFresh)
reStreak.place(x=width/2 - 40, y=140)

with open("Streak.txt", "r") as file:
    content = file.read()

    streak = int(content.split("Streak - ")[1].split("\n")[0])
    highscore = int(content.split("Highscore - ")[1])

print("Streak:", streak)
print("Highscore:", highscore)

app.mainloop()
