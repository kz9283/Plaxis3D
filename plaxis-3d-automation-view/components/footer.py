from tkinter import Frame, Label, Button

class Footer(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.backButton = Button(self, text='Back', padx=10, pady=5, bg="RoyalBlue1")
        self.nextButton = Button(self, text='Next', padx=10, pady=5, bg="RoyalBlue1")
        self.pageNum = Label(self, text="Page X of X")

        self.backButton.grid(row=0, column=0)
        self.pageNum.grid(row=0, column=1)
        self.nextButton.grid(row=0, column=2)

