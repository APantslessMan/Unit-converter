from tkinter import *

previous_from = 0
previous_to = 0
###
#   Functions
###


def enter_unit_convert(event, to_from):
    global previous_to, previous_from
    if to_from == 0:
        button.config(text="Convert-->", state='normal')
        to_input.delete(0, END)
        previous_from = int(from_input.get())

    elif to_from == 1:
        button.config(text="<--Convert", state='normal')
        from_input.delete(0, END)
        previous_to = int(to_input.get())

    else:
        button.config(state='disabled')

# def to_select(event):
#     global to_select, from_select
#     from_select = 0
#     to_select = 1
#     enter_unit_convert()
# def from_select(event):
#     global to_select, from_select
#     to_select = 0
#     from_select = 1
def radio_used():
    if radio_state.get() == 1:
        from_units.config(values=list(reversed(distance_units)))
        from_sb_var.set(distance_units[0])
        to_units.config(values=list(reversed(distance_units)))
        to_sb_var.set(distance_units[5])
    if radio_state.get() == 2:
        from_units.config(values=list(reversed(volume_units)))
        from_sb_var.set(volume_units[0])
        to_units.config(values=list(reversed(volume_units)))
        to_sb_var.set(volume_units[3])
    if radio_state.get() == 3:
        from_units.config(values=list(reversed(weight_units)))
        from_sb_var.set(weight_units[2])
        to_units.config(values=list(reversed(weight_units)))
        to_sb_var.set(weight_units[6])

def click_convert():
    global convert_state, previous_from, previous_to
    # TODO instead of static values for KM and Mile, we change depending on spinbox selection
    # create Dict with structure { Distance: { km: { mile: "0.621371" , "foot": "3280.8398950131" }, "Mile...
    # we can also dynamically load the units from a json file maybe?
    # If state 0 then change 'From' side to 'To' side * 'from' sides multiplier
    # e.g. Miles to km is 1.60934
    if convert_state == 0:
        from_input.insert(END, string=f"{previous_to * 1.60934}")
        convert_state = 1


        return
    # If state 1 then change 'To' side to 'From' side * 'to' sides multiplier
    # e.g. KM to Miles is 0.621371
    if convert_state == 1:
        print(previous_from)
        to_input.insert(END, string=f"{previous_from * 0.621371}")
        convert_state = 0

        return

# create window object
window = Tk()
window.title("Unit Converter")
window.minsize(width=500, height=300)
window.configure(bg='#004d84')

# frame

sep = Frame(window, bg="#ffaa00")
sep.place(x=0, y=0, relwidth=1, relheight=0.2)


# Top Label

label = Label(bg='#ffaa00', fg='#003366', text="Unit Converter", font=("gill sans", 28, "bold"))
label.place(y=10, x=200)
#
# radio blank radio
# dial  blank dial
# from  conv  to
#       calc


# 3 radios, Distance, volume, weight
radio_state = IntVar()
radio_distance = Radiobutton(bg="#002b4d", fg="#ffaa00", highlightbackground="#002b4d", selectcolor="#004d84",
                             text="Distance", value=1, variable=radio_state, command=radio_used, height=1, width=12,
                             indicatoron=0, font=("gill sans", 15, "bold"))
radio_volume = Radiobutton(bg="#002b4d", fg="#ffaa00", highlightbackground="#002b4d", selectcolor="#004d84",
                           text="Volume", value=2, variable=radio_state, command=radio_used, height=1, width=12,
                           indicatoron=0, font=("gill sans", 15, "bold"))
radio_weight = Radiobutton(bg="#002b4d", fg="#ffaa00", highlightbackground="#002b4d", selectcolor="#004d84",
                           text="Weight", value=3, variable=radio_state, command=radio_used, height=1, width=12,
                           indicatoron=0, font=("gill sans", 15, "bold"))
radio_distance.place(y=80, x=20)
radio_volume.place(y=80, x=170)
radio_weight.place(y=80, x=320)


# 2 dials: Holds each of the units from the radios
distance_units = ["Km", "M", "Cm", "mm", "μm", "Mile", "Foot", "Inch", "Yard", "Rod", "AU", "Light Year"]
volume_units = ["Cup", "Tbsp", "tsp", "ml", "Cubic Meter", "brl", "Litre", "Gallon", "Pint", "Cubic Inch", "Cubic CM"]
weight_units = ["Gt", "t", "Kg", "G", "mg", "µg", "lb", "oz"]
from_sb_var = StringVar()
to_sb_var = StringVar()
from_units = Spinbox(window, width=12, font=("gill sans", 12, "bold"), textvariable=from_sb_var, values=list(reversed(distance_units)))
from_sb_var.set(distance_units[0])
to_units = Spinbox(window, width=12, font=("gill sans", 12, "bold"), textvariable=to_sb_var, values=list(reversed(distance_units)))
to_sb_var.set(distance_units[5])
from_units.place(y=130, x=30)
to_units.place(y=130, x=340)
# input from
from_input = Entry(bg="#ffaa00", width=10, font=("gill sans", 20, "bold"))
#Add some text to begin with
#from_input.insert(END, string="1")
#Gets text in entry
print(from_input.get())
from_input.place(y=160, x=20)
from_input.bind('<KeyRelease>', lambda event: enter_unit_convert(event, 0))


# input to
#to_input = Entry()
to_input = Entry(bg="#ffaa00", width=10, font=("gill sans", 20, "bold"))
#Add some text to begin with
#to_input.insert(END, string=f"{float(from_input.get()) * 1.609}")
#Gets text in entry
print(from_input.get())
to_input.place(y=160, x=315)
to_input.bind('<KeyRelease>', lambda event: enter_unit_convert(event, 1))


# convert button
convert_state = 0
#button = Button(text="Click me", command=click_convert)
button = Button(text="Convert-->", command=click_convert, state="disabled",  height=1, width=10, font=("gill sans", 14, "bold"))
button.place(y=160, x=180)

window.mainloop()
