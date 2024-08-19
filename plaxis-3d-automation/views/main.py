from .root import Root
from .geometry import GeometryView
from .soil_material import SoilMatView
from .soil_layer import SoilLayerView

class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self._add_frames(SoilMatView, "soilmat")
        self._add_frames(SoilLayerView, "layer")
        self._add_frames(GeometryView, "geometry")

    def _add_frames(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky='nsew')

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()