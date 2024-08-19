# from models.main import Model
from views.main import View
from models.main import Model

from .geometry import GeometryController
from .soilmat import SoilMaterialController
from .layer import SoilLayerController
from .generate import GenerateController

class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.geometryController = GeometryController(model, view)
        self.soilMatController = SoilMaterialController(model, view)
        self.soilLayerController = SoilLayerController(model, view)
        self.soilMatController = GenerateController(model, view)

        self.model.soil_mats.add_event_listener(
            'soil_mats_defined', self.soil_mat_defined_listener
            )
        
        self.model.soil_mats.add_event_listener(
            'soil_layers_defined', self.soil_layer_defined_listener
            )
        
    def soil_mat_defined_listener(self, data):
        data.add_soil_mat()
        print("Soil Material Defined")
    
    def soil_layer_defined_listener(self, data):
        data.add_soil_layer()
        print("Soil Layer Defined")

    def start(self):
        self.view.start_mainloop()
