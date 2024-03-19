import numpy as np
from data.vars import Variables

class UserData(object):
    def __init__(self):

        self.xmin = 0.0                 # [m]
        self.xmax = 25400000.0 - 100000 # [m]
        self.Nx = 254

        self.ymin = 0.0                 # [m]
        self.ymax = 5000000.0 - 100000  # [m]
        self.Ny = 50

        self.dt = 60.0                  # [s]
        self.T = 4.0 * 24.0 * 3600.0    # [s]    

        self.g = 9.81                   # [m/s^2]
        self.f = 0.0                    # [s^(-1)]

    
def sol_init(sg):
    std_blob = 8.0*sg.dy; # Standard deviation of blob (m)
    height = 9750. + 1000.*np.exp(-((sg.xg-0.25*np.mean(sg.x))**2.+(sg.yg-np.mean(sg.y))**2.)/(2.* \
                                                     std_blob**2.))

    # this creates the solution container
    sol = Variables(sg)
    sol.h[...] = height

    return sol