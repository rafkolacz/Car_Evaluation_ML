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
        for i in range(6):
            self.InitUI(i)
            print(i)
        self.Button()


    def calculate(self):
        self.result = ttk.Label(self, text="Car class is " + self.value.get())
        data = [self.valueB.get(),self.valueM.get(),self.valueD.get(),self.valueP.get(),self.valueL.get(),self.valueS.get()]
        print(data)
        print(self.valueS.get())
        self.result.grid(column=1, row=8)
        # print(Car_Evaluation.engine(data))

    def InitUI(self, row):
        self.value = StringVar()
        self.valueB = StringVar()
        self.valueD = StringVar()
        self.valueP = StringVar()
        self.valueM = StringVar()
        self.valueL = StringVar()
        self.valueS = StringVar()

        self.combo = ttk.Combobox(self, width=15, textvariable=self.value)
        if row == 0 or row == 1:
            self.combo['values'] = ('low', 'med', 'high', 'vhigh')
            if row == 0:
                name = "buying price"
                self.combo.configure(textvariable=self.valueB)
            else:
                name = "price of the maintenance"
                self.combo.configure(textvariable=self.valueM)
        if row == 2 or row == 3:
            self.combo['values'] = (2, 3, 4, 5, 'more')
            if row == 2:
                name = "number of doors"
                self.combo.configure(textvariable=self.valueD)
            else:
                name = "capacity in terms of persons to carry"
                self.combo.configure(textvariable=self.valueP)
        if row == 4:
            self.combo['values'] = ('small', 'med', 'big')
            name = "size of luggage boot"
            self.combo.configure(textvariable=self.valueL)
        if row == 5:
            self.combo['values'] = ('low', 'med', 'high')
            name = "estimated safety of the car"
            self.combo.configure(textvariable=self.valueS)

        self.combo.grid(column=1, row=row+1)
        self.label = ttk.Label(self, text = "Select " + name)
        self.label.grid(column=0, row=row+1)

    def Button(self):
        self.button = ttk.Button(self, text="Submit", command=self.calculate)
        self.button.grid(column=1, row=7)

root = Root()
root.mainloop()
