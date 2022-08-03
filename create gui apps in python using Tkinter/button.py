from tkinter import *

root = Tk()
# create obj and pass root
newframe = Frame(root)
# puts created frame on window
newframe.pack()

# create obj and pass root
otherframe = Frame(root)
# puts created frame on window in bottom
otherframe.pack(side=BOTTOM)

# create a button in new Frame
button1 = Button(newframe, text="Click Here", fg="Red")
button2 = Button(otherframe, text="Click Here", fg="blue")

button1.pack()
button2.pack()

root.mainloop()