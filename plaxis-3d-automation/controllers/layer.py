from tkinter import StringVar, OptionMenu, Entry, Frame

class SoilLayerInput:
    def __init__(self, model, soilLayerFrame):
        self.SOIL_MAT_LIST = [key for key in model.soil_mats.soil_mat_dict]

        self.layer = Frame(soilLayerFrame)

        self.layerName = StringVar()
        self.layerName.set('Select soil unit')
        drop = OptionMenu(self.layer, self.layerName, *self.SOIL_MAT_LIST)
        drop.grid(row=0, column=0)

        self.elevation = Entry(self.layer, borderwidth=2)
        self.elevation.grid(row=0, column=1)

        self.layer.pack()

class SoilLayerController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames['layer']
        self._bind()

    def _bind(self):
        self.frame.addLayerButton.config(command=self.add_layer)
        self.frame.footer.nextButton.config(command=self.next_page)
        self.frame.footer.backButton.config(command=self.last_page)
        
    def add_layer(self):
        soil_layer_input = SoilLayerInput(self.model, self.frame.soilLayerFrame)
        self.model.soil_mats.soil_layer_inputs.append(soil_layer_input)

    def next_page(self):
        self.view.switch('layer')

    def last_page(self):
        self.view.switch('soilmat')