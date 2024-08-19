from tkinter import Frame, Label, Entry, Button, BooleanVar, Checkbutton, IntVar, Radiobutton
from .components.footer import Footer

class SoilMatView(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.soilMatFrame = Frame(self)

        self.heading = Frame(self.soilMatFrame)

        Label(self.heading, text='Soil Unit', width=12).grid(row=0, column=0)
        Label(self.heading, text=' Gamma (kN/m3)',width=15).grid(row=0, column=1)
        Label(self.heading, text='c\' (kPa) ', width=10).grid(row=0, column=2)
        Label(self.heading, text='phi\'(deg)', width=10).grid(row=0, column=3)
        Label(self.heading, text='E\'(MPa)', width=10).grid(row=0, column=4)
        Label(self.heading, text='v ', width=10).grid(row=0, column=5)
        self.heading.pack()
        self.soilMatFrame.pack()

        self.addMaterialButton = Button(self, text='Add Material', padx=10, pady=5)
        self.addMaterialButton.pack()

        self.footer = Footer(self)
        self.footer.pack()

        

