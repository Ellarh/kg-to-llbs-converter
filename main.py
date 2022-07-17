from tkinter import *
from tkinter import messagebox

LIGHT_CORAL = "#F08080"
LIGHT_SALMON = "#FFA07A"
RED = "#FF0000"
PURPLE = "#cc99ff"
DARK_GREEN = "#001a00"
FONT = "Lora"


window = Tk()
window.title("UNIT CONVERTER TOOL")
window.config(padx=15, pady=20)


canvas = Canvas()
image = PhotoImage(file="fruit.png")
canvas.create_image(200, 160, image=image)
canvas.grid(column=1, row=1)

# Calculate Function
def calculate():
    try:
        kg = int(kg_input.get())
        total = round(kg * 2.2)
    except ValueError:
        messagebox.showinfo(title="Number Needed", message="You need to use a number to convert.")
    else:
        pound_entry.config(text=total)
        title.config(text="Converted", fg=DARK_GREEN)

# --------------------------------------UI DESIGN---------------------------------------------------

# Labels
title = Label(text="UNIT CONVERTER", font=(FONT, 30, "bold"))
title.grid(column=1, row=0)

from_title = Label(text="From:", font=(FONT, 15))
from_title.grid(column=0, row=2)

pounds_lable = Label(text="Llbs", font=(FONT, 15))
pounds_lable.grid(column=2, row=3)

pound_entry = Label(text="0", font=(FONT, 15))
pound_entry.grid(column=1, row=3)

to_label = Label(text="To", font=(FONT, 15))
to_label.grid(column=0, row=3)

kg_label = Label(text="Kg", font=(FONT, 15))
kg_label.grid(column=2, row=2)



# Entry
kg_input = Entry(width=30)
kg_input.grid(column=1, row=2)
kg_input.focus()

# Button
calculate_button = Button(width=10, text="Calculate", font=(FONT, 12, "bold"), command=calculate)
calculate_button.grid(column=1, row=4)
window.mainloop()
