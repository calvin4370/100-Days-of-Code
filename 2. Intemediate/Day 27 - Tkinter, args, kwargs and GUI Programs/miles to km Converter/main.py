from tkinter import *

window = Tk()
window.title("miles to km Converter")
window.minsize(width=300, height=300)

miles_label = Label(text="miles", font=("Times New Roman", 16, "normal"), pady=20)
equal_label = Label(text="is equals to", font=("Times New Roman", 16, "normal"), pady=30)
km_label = Label(text="km", font=("Times New Roman", 16, "normal"), pady=30)
km_result = Label(text="", font=("Times New Roman", 16, "normal"), pady=30)

miles_input = Entry(width=16, font=("Calibri", 16, "bold"))

def write_km():
    miles = int(miles_input.get())

    km_result["text"] = round(miles * 1.609)

convert_button = Button(text="convert", command=write_km)

miles_label.grid(column=3, row=1)
equal_label.grid(column=1, row=2)
km_label.grid(column=3, row=2)
km_result.grid(column=2, row=2)
miles_input.grid(column=2, row=1)
convert_button.grid(column=2, row=3)


window.mainloop()


