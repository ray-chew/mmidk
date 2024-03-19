import numpy as np

class Variables(object):
    def __init__(self, sg):
        self.h = np.zeros_like(sg.xg)
        self.u = np.zeros_like(sg.xg)
        self.v = np.zeros_like(sg.xg)
        self.squeezer()
        

    def flip(self):
        for key, value in vars(self).items():
            setattr(self, key, np.moveaxis(value,0,-1))


    def squeezer(self):
        for key, value in vars(self).items():
            setattr(self,key,value.squeeze())