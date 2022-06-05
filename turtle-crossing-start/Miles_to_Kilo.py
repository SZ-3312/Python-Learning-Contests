from tkinter import *


def mile_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 3)
    result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)
window.minsize(width=400, height=100)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=3, row=0)

result_label = Label(text="0")
result_label.grid(column=4, row=0)

kilometers_label = Label(text="km")
kilometers_label.grid(column=5, row=0)

calculate_button = Button(text="Calculate", background="light yellow", command=mile_to_km)
calculate_button.grid(column=3, row=2)

if __name__ == "__main__":
    window.mainloop()
