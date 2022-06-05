from tkinter import *
window = Tk()
window.title("Click the Button!")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)
score = 1


def print_label():
    global score
    my_label = Label(text=f"Score: {score}", font=("Arial", 24, "italic"))
    my_label.place(x=0, y=0)
    score += 1


button = Button(text="Click to SCORE", command=print_label, background="gold")
button.place(x=240, y=140)

if __name__ == '__main__':
    window.mainloop()
