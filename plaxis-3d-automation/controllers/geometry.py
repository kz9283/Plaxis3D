from tkinter import StringVar, OptionMenu, Entry, Frame

OPERATION_MODE_LIST = ["Standing", "Extracting", "Moving"]

class GeometryController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames['geometry']
        self._bind()

    def _bind(self):
        self.frame.addModeButton.config(command=self.add_operation_mode)
        self.frame.footer.nextButton.config(command=self.next_page)
        
    def add_operation_mode(self):

        self.mode = Frame(self.frame.geometryFrame)
        operationMode = StringVar()
        operationMode.set('Select mode')
        drop = OptionMenu(self.mode, operationMode, *OPERATION_MODE_LIST)
        drop.grid(row=0, column=0)

        length_L = Entry(self.mode, borderwidth=2)
        length_L.grid(row=0, column=1)
        width_B = Entry(self.mode, borderwidth=2)
        width_B.grid(row=0, column=2)

        self.mode.pack()

    def next_page(self):
        self.view.switch('soilmat')
