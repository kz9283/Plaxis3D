class SimpleProject:
    """
    Class that provides a way to quickly setup a project
    """
    def __init__(self):

        from plxscripting.easy import new_server
        self._new_server = new_server
        self._s_i, self._g_i = self._new_server('localhost', 10000, password='aaaaaa', timeout=10.0)

    @property
    def g_i(self):
        return self._g_i
    
    def start_new_server(self):
        self._s_i.new()
        self._g_i.setproperties('UnitTime', 's') # Change project unit to time

    def add_soil_mat(self, soil_mat_input_dict:dict):
        
        SOIL_PARAMS = [
            ('Identification', soil_mat_input_dict['identification']),
            ('SoilModel', 2), # Mohr Coulomb
            ('gammaUnsat', soil_mat_input_dict['gamma']),
            ('gammaSat', soil_mat_input_dict['gamma']),
            ('nu', soil_mat_input_dict['poissonRatio']),
            ('Rinter', 0.67),
            ('InterfaceStrengthDetermination', 'manual'),
            ('cRef', soil_mat_input_dict['cPrime']),
            ('Eref', soil_mat_input_dict['EPrime']),
            ('phi', soil_mat_input_dict['phiPrime'])
        ]

        soilmat = self._g_i.soilmat(*SOIL_PARAMS)
        return soilmat
    
    def add_soil_profile(self, soil_layer_dict:dict):

        borehole = self._g_i.borehole(0, 0)

        for i, soil_layer in enumerate(soil_layer_dict):

            if i != len(soil_layer_dict):
                self._g_i.soillayer(0)
            self._g_i.setsoillayerlevel(borehole, i, soil_layer_dict[soil_layer])




