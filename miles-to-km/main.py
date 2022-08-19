import tkinter


def calculate_km():
    miles = float(miles_input.get())
    km_value_label.config(text=miles * 1.609)


window = tkinter.Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

miles_input = tkinter.Entry()
miles_input.config(width=10)
miles_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

km_value_label = tkinter.Label(text=0)
km_value_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

calc_button = tkinter.Button(text="Calculate", command=calculate_km)
calc_button.grid(row=2, column=1)

window.mainloop()