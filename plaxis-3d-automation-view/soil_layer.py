from tkinter import Frame, Label, Entry, Button, BooleanVar, Checkbutton, IntVar, Radiobutton
from components.footer import Footer

class SoilLayerView(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.soilLayerFrame = Frame(self)

        self.heading = Frame(self.soilLayerFrame)

        Label(self.heading, text='Soil Unit   |').grid(row=0, column=0)
        Label(self.heading, text='   Elevation (mRL)   ').grid(row=0, column=1)
       
        self.heading.pack()
        self.soilLayerFrame.pack()

        self.addLayerButton = Button(self, text='Add Soil Layer', padx=10, pady=5)
        self.addLayerButton.pack()

        self.footer = Footer(self)
        self.footer.pack()

        self.generateButton = Button(self, text='Generate', padx=10, pady=5, bg="RoyalBlue1")
        self.generateButton.pack()



    