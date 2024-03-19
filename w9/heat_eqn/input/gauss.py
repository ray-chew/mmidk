import numpy as np
from data.vars import Variables

class UserData(object):
    def __init__(self):

        self.xmin = -4.0
        self.xmax = +4.0
        self.Nx = 81

        self.ymin = -4.0
        self.ymax = +4.0
        self.Ny = 81

        self.dt = 0.001
        self.T = 1.0

    
def sol_init(sg):
    sol = Variables(sg)
    sol.u[...] = np.exp(-(sg.x**2 + sg.y**2)).squeeze()

    return sol