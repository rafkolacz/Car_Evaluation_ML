from tkinter import *
from tkinter import ttk
import Car_Evaluation


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Car Evaluation")
        self.minsize(400,200)
        self.welcomeLabel = ttk.Label(self, text="Hello and welcome in Car Evaluation App")
        self.welcomeLabel.grid(column=0, row=0)
        for i in range(5):
            self.InitUI(i)
        self.Button()


    def calculate(self):
        self.result = ttk.Label(self, text="Car class is " + self.value.get())
        self.result.grid(column=1, row=8)
        # print(Car_Evaluation.engine(data))

    def InitUI(self, row):
        self.value = StringVar()
        self.combo = ttk.Combobox(self, width=15, textvariable=self.value)
        if row == 0 or row == 1:
            self.combo['values'] = ('low', 'med', 'high', 'vhigh')
            if row == 0:
                name = "buying price"
            else:
                name = "price of the maintenance"
        if row == 2 or row == 3:
            self.combo['values'] = (2, 3, 4, 5, 'more')
            if row == 2:
                name = "number of doors"
            else:
                name = "capacity in terms of persons to carry"
        if row == 4:
            self.combo['values'] = ('small', 'med', 'big')
            name = "size of luggage boot"
        if row == 5:
            self.combo['values'] = ('low', 'med', 'high')
            name = "estimated safety of the car"

        self.combo.grid(column=1, row=row+1)
        self.label = ttk.Label(self, text = "Select " + name)
        self.label.grid(column=0, row=row+1)

    def Button(self):
        self.button = ttk.Button(self, text="Submit", command=self.calculate)
        self.button.grid(column=1, row=7)

root = Root()
root.mainloop()
