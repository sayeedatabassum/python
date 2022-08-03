from tkinter import *

class MyButtons:
    
    def __init__(self, rootone):
        # adding frame on window
        frame = Frame(rootone)
        frame.pack()
        
        # create button
        self.printbutton = Button(frame, text="Click Here", command=self.printmessage)
        # put button on window
        self.printbutton.pack()
        
        # exit particular window
        self.quitbutton = Button(frame, text="Exit", command= frame.quit)
        self.quitbutton.pack(side=LEFT)
        
    def printmessage(self):
        print("Button Clicked")
        
root = Tk()
b = MyButtons(root)
root.mainloop()