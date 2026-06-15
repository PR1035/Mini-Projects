import sys
v = sys.version
from tkinter import *
from tkinter import filedialog


root = Tk("Text editor")
text = Text(root)
# text.grid()

#Light and Dark Mode
light = PhotoImage(file="TextEditor/light.png").subsample(8, 8)
dark = PhotoImage(file="TextEditor/dark.png").subsample(12, 12)
switch_value = True

def toggle():
    global switch_value
    if switch_value == True:
        switch.config(image=dark, bg="#26242f", activebackground="#26242f")
        root.config(bg="#26242f")
        text.config(bg="#1e1e1e", fg="white", insertbackground="white")
        switch_value = False

    else:
        switch.config(image=light, bg="white", activebackground="white")
        root.config(bg="white")
        text.config(bg="white", fg="black", insertbackground="black")
        switch_value = True



switch = Button(root, image=light, bd=0, bg="white", activebackground="white", command=toggle)
# switch.grid(padx=50, pady = 150)

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()
button = Button(root, text="Save", command=saveas)
# button.grid()

def FontHelvetica():
        global text
        text.config(font= "Helvetica")
def FontCourier():
      global text
      text.config(font="Courier")
font = Menubutton(root, text="Font")
# font.grid()
font.menu = Menu(font, tearoff=0)
font['menu'] = font.menu
helvetica = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier,command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,command=FontHelvetica)

text.grid(row=0, column=0, columnspan=2)
switch.grid(row=1, column=0, pady=10)
button.grid(row=1, column=1, pady=10)
font.grid(row=2, column=0, pady=10)

root.mainloop()