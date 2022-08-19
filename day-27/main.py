import tkinter


def button_clicked():
    new_text = text_input.get()
    my_label.config(text= new_text)


# Create window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Create label
my_label = tkinter.Label(text="Text Written here", font=("Arial", 20, "bold"))
my_label.grid(row=0, column=0)

# Create a textbox
text_input = tkinter.Entry()
text_input.grid(row=2, column=3)


# Create button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# New button
new_button = tkinter.Button(text="Don't Click me", command=button_clicked)
new_button.grid(row=0, column=2)







window.mainloop()

