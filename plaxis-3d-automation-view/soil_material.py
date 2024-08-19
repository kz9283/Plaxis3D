from tkinter import Frame, Label, Entry, Button, BooleanVar, Checkbutton, IntVar, Radiobutton
from components.footer import Footer

class SoilMatView(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.soilMatFrame = Frame(self)

        self.heading = Frame(self.soilMatFrame)

        Label(self.heading, text='Soil Unit   |').grid(row=0, column=0,  padx=10, pady=5, sticky='w')
        Label(self.heading, text='   Gamma (kN/m3)   |').grid(row=0, column=1, padx=10, pady=5, sticky='w')
        Label(self.heading, text='   c\' (kPa)   |').grid(row=0, column=2, padx=10, pady=5, sticky='w')
        Label(self.heading, text='   phi\' (deg)   |').grid(row=0, column=3, padx=10, pady=5, sticky='w')
        Label(self.heading, text='   E\' (MPa)   |').grid(row=0, column=4)
        Label(self.heading, text='   v   ').grid(row=0, column=5)
        self.heading.pack()
        self.soilMatFrame.pack()

        self.addMaterialButton = Button(self, text='Add Material', padx=10, pady=5)
        self.addMaterialButton.pack()

        self.footer = Footer(self)
        self.footer.pack()

        self.generateButton = Button(self, text='Generate', padx=10, pady=5, bg="RoyalBlue1")
        self.generateButton.pack()

