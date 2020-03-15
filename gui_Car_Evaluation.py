from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self)
        self.title("Car Evaluation")
        # self.minsize()
        #self.InitUI()

    def InitUI(self):
        self.value = StringVar()

        self.combo = ttk.Combobox(self, width = 15, textvariable = self.value)






root = Root()
root.mainloop()