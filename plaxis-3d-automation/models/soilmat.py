from .helper import cleanOneValue
from .base import ObservableModel

class SoilMaterials(ObservableModel):

    def __init__(self):
        super().__init__()
        self.soil_mat_inputs = []
        self.soil_layer_inputs = []
        self.num_rows = 0
        self.soil_mat_dict = {}
        self.soil_layer_dict = {}

    def add_soil_mat(self):
        
        for row in self.soil_mat_inputs:
            materialName = row.materialName.get()

            # Create dictionary of material properties for each material
            _dict = {}
            _dict['identification'] = materialName
            _dict['gamma'] = cleanOneValue(row.gamma.get())
            _dict['cPrime'] = cleanOneValue(row.cPrime.get())
            _dict['EPrime'] = cleanOneValue(row.EPrime.get()) * 1000 # convert MPa to kPa
            _dict['phiPrime'] = cleanOneValue(row.phiPrime.get())
            _dict['poissonRatio'] = cleanOneValue(row.poissonRatio.get())

            # Assign _dict to soil_mat_dict with materialName as key
            self.soil_mat_dict[materialName] = _dict

    def add_soil_layer(self):

        for row in self.soil_layer_inputs:

            # Populate soil_layer_dict
            layerName = row.layerName.get()
            self.soil_layer_dict[layerName] = cleanOneValue(row.elevation.get())