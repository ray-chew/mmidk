import numpy as np
from data.vars import Variables

class UserData(object):
    def __init__(self):

        self.xmin = 0.0
        self.xmax = 25400000.0 - 100000
        self.Nx = 254+0

        self.ymin = 0.0
        self.ymax = 5000000.0 - 100000
        self.Ny = 50+0

        self.dt = 60.0
        self.T = 4*24.0*60*60

        self.g = 9.81
        self.f = 0.0

        self.fn = 'gravity_wave'
        self.output_interval = 60*60

    
def sol_init(sg, ud):
    std_blob = 8.0*sg.dy
    height = 9750. + 1000.*np.exp(-((sg.xg-0.25*np.mean(sg.x))**2.+(sg.yg-np.mean(sg.y))**2.)/(2.*std_blob**2.))

    sol = Variables(sg)
    sol.h[...] = height
    sol.u[...] = 0.0
    sol.v[...] = 0.0

    sol.H = np.zeros_like(sol.h)
    sol.F = np.zeros_like(sol.h)

    return sol