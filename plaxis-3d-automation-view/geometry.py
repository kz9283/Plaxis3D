from tkinter import Frame, Label, Entry, Button, BooleanVar, Checkbutton, IntVar, Radiobutton
from components.footer import Footer

class GeometryView(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometryFrame = Frame(self)

        self.heading = Frame(self.geometryFrame)

        Label(self.heading, text='Operation Mode    |').grid(row=0, column=0)
        Label(self.heading, text='    Length L (m)    |').grid(row=0, column=1)
        Label(self.heading, text='    Width B (m)').grid(row=0, column=2)
        self.heading.pack()
        self.geometryFrame.pack()

        self.addModeButton = Button(self, text='Add operation mode', padx=10, pady=5)
        self.addModeButton.pack()

        self.footer = Footer(self)
        self.footer.pack()
