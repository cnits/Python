__author__ = 'PhongVu'
from Tkinter import *


master = Tk()

canvas = Canvas(master, width=400, height=300, bg="gray")
canvas.create_line((0, 150, 400, 150), fill="#054000", width=3)
canvas.create_text((200, 135), activefill="Green", fill="red", text="TTTTTTTTTTTt")
canvas.create_rectangle((135, 125, 270, 145))

v = StringVar()
u = StringVar()
Label(master, textvariable=v, bd=1, font=("Helvetica", 16),
      fg="red", bg="purple").pack(side=BOTTOM, padx=2, pady=2)
Label(master, textvariable=u, bd=1, font=("Helvetica", 16),
      fg="red", bg="purple").pack(side=TOP, padx=2, pady=2)
v.set("G-Team")
u.set("R-Team")
canvas.pack(fill=BOTH)

mainloop()