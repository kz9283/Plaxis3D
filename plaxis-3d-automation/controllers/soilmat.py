from tkinter import StringVar, OptionMenu, Entry, Frame

class SoilMatInput:
    def __init__(self, soilMatFrame):
        self.material = Frame(soilMatFrame)

        self.materialName = Entry(self.material, width=12)
        self.materialName.grid(row=0, column=0)
        self.gamma = Entry(self.material,width=17)
        self.gamma.grid(row=0, column=1)
        self.cPrime = Entry(self.material, width=11)
        self.cPrime.grid(row=0, column=2)
        self.phiPrime = Entry(self.material, width=12)
        self.phiPrime.grid(row=0, column=3)
        self.EPrime = Entry(self.material, width=12)
        self.EPrime.grid(row=0, column=4)
        self.poissonRatio = Entry(self.material, width=8)
        self.poissonRatio.grid(row=0, column=5)

        self.material.pack()

    def prefilled_input(self):

        # For testing purpose
        self.materialName.insert(0, 'sand')
        self.gamma.insert(0, '19')
        self.cPrime.insert(0, '2')
        self.phiPrime.insert(0, '30')
        self.EPrime.insert(0, '20')
        self.poissonRatio.insert(0, '0.3')

class SoilMaterialController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames['soilmat']
        self._bind()

    def _bind(self):
        self.frame.addMaterialButton.config(command=self.add_material)
        self.frame.footer.nextButton.config(command=self.next_page)
        self.frame.footer.backButton.config(command=self.last_page)
        
    def add_material(self):
        soil_mat_input = SoilMatInput(self.frame.soilMatFrame)
        soil_mat_input.prefilled_input() # to delete in production
        self.model.soil_mats.soil_mat_inputs.append(soil_mat_input)       

    def next_page(self):
        self.view.switch('layer')
        self.model.soil_mats.trigger_event("soil_mats_defined")
        
    def last_page(self):
        self.view.switch('geometry')