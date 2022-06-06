from tkinter import *
from time import *
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


def restart():
    global reps
    reps = 1
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_marks.config(text="")


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        title.config(text="Break", fg=RED)

    elif reps % 2 == 1:
        countdown(work_sec)
        title.config(text="Work", fg=GREEN)

    else:
        countdown(short_break)
        title.config(text="Break", fg=PINK)

    reps += 1


def countdown(count):
    global timer, reps
    seconds = count % 60
    minutes = (count - seconds) // 60

    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"

    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        if work_sessions > 4:
            work_sessions = 0
            reps = 1

        for i in range(work_sessions):
            marks += "✔ "
        check_marks.config(text=marks)


# User Interface
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

canvas = Canvas(width=260, height=250, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(125, 120, image=tomato)
timer_text = canvas.create_text(125, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=restart)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


if __name__ == "__main__":
    window.mainloop()
