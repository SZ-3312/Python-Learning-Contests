from tkinter import *
# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Timer Reset

# Timer Mechanism

# Countdown Mechanism

# UI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

canvas = Canvas(width=260, height=250)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(125, 120, image=tomato)
canvas.pack()


if __name__ == "__main__":
    window.mainloop()