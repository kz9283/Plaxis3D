from models.simple_project import SimpleProject
from models.helper import cleanOneValue

class GenerateController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames['layer']
        self._bind()

    def _bind(self):
        try:
            self.frame.generateButton.config(command=self.generateModel)
        except:
            pass

    def generateModel(self):

        self.model.soil_mats.trigger_event('soil_layers_defined')

        print("GENERATING...")
        project = self.model.project
        project.start_new_server()

        # Code to perform Plaxis functions
        self.applyProjectDetails()

    def applyProjectDetails(self):
        
        self.addSoilMaterial()
        self.addSoilLayers()
        self.assignSoilMat()

    def addSoilMaterial(self):

        # Add soil material
        for key in self.model.soil_mats.soil_mat_dict:
            _dict = self.model.soil_mats.soil_mat_dict[key]
            plaxisSoilMat_obj = self.model.project.add_soil_mat(_dict)
            
    def addSoilLayers(self):
        self.model.project.add_soil_profile(self.model.soil_mats.soil_layer_dict)

    def assignSoilMat(self):
        pass





    
