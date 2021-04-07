import tkinter as tk
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


pest_points = 1
void_top = 250
void_bottom = 250
mel_helm = 200
mag_helm = 200
ran_helm = 200
elite = 200

# initialize tkinter
root = Tk()
app = Window(root)

canvas1 = tk.Canvas(root, width=500, height=500)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 240, window=entry1)


def getPestPoints():
    global pest_points
    pest_points = entry1.get()
    print(pest_points)

    label3 = tk.Label(root, text='Your current points are:')
    canvas1.create_window(100, 10, window=label3)

    label1 = tk.Label(root, text=pest_points)
    canvas1.create_window(100, 30, window=label1)


def voidmath():
    global pest_points
    for_all_void = (void_top + void_bottom + mel_helm + mag_helm + ran_helm) - int(pest_points)
    remaining = int(for_all_void) / 5


    if (mhelm.get() == 1):
        for_all_void = for_all_void - mel_helm
    if (mghelm.get() == 1):
        for_all_void = for_all_void - mag_helm
    if (rnghelm.get() == 1):
        for_all_void = for_all_void - ran_helm

    label4 = tk.Label(root, text='For full set of void armor: ' + str(for_all_void))
    canvas1.create_window(200, 110, window=label4)

    print(mhelm.get())


    label5 = tk.Label(root, text='Remaining Veteran games: ' + str(remaining))
    canvas1.create_window(200, 130, window=label5)


button1 = tk.Button(text='Submit', command=getPestPoints)
canvas1.create_window(200, 280, window=button1)

button2 = tk.Button(text='For Void Armor', command=voidmath)
canvas1.create_window(100, 280, window=button2)

mhelm = tk.IntVar()
mghelm = tk.IntVar()
rnghelm = tk.IntVar()
vbody = tk.IntVar()
vlegs = tk.IntVar()

chhelmmel = tk.Checkbutton(root, text='Melee Helm', variable=mhelm)
chhelmmel.place(x=10, y=60)
chhelmmag = tk.Checkbutton(root, text='Magic Helm', variable=mghelm)
chhelmmag.place(x=10, y=90)
chhelmran = tk.Checkbutton(root, text='Ranged Helm', variable=rnghelm)
chhelmran.place(x=10, y=120)
chbody = tk.Checkbutton(root, text='Void Body', variable=vbody)
chbody.place(x=10, y=150)
chlegs = tk.Checkbutton(root, text='Void Legs', variable=vlegs)
chlegs.place(x=10, y=180)

# set window title
root.wm_title("OSRS Tools")

# show window
root.mainloop()
