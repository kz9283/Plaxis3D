from .soilmat import SoilMaterials
from .simple_project import SimpleProject

class Model:
    def __init__(self):
        self.soil_mats = SoilMaterials()
        #self.project = SimpleProject()