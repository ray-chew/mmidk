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
        self.f = 1e-4                    # [s^(-1)]
        self.beta = 1.6e-11

    
def sol_init(sg,ud):
    # zonal jet
    height = 10000. - np.tanh(20.0*((sg.yg-np.mean(sg.y))/np.max(sg.y)))*400.

    F = ud.f+ud.beta*(sg.yg-np.mean(sg.y))

    # add random noise to the height field
    r,c=np.shape(height)
    height = height + 1.0*np.random.randn(r,c)*(sg.dx/1.0e5)*(np.abs(F)/1e-4)

    height = height.T
    F = F.T
    u = np.zeros_like(height)
    v = np.zeros_like(height)

    # initial geostrophic
    u[:,1:-1] = -(0.5*ud.g/(F[:,1:-1]*sg.dx)) * (height[:,2:]-height[:,0:-2])
    v[1:-1,:] = (0.5*ud.g/(F[1:-1,:]*sg.dx))  * (height[2:,:]-height[0:-2,:])
    # Zonal wind is periodic so set u(1) and u(end) as dummy points that
    # replicate u(end-1) and u(2), respectively
    u[[0 ,-1],:] = u[[1 ,-2],:]
    # Meridional wind must be zero at the north and south edges of the
    # channel 
    v[:,[0, -1]] = 0.

    # Don't allow the initial wind speed to exceed 200 m/s anywhere
    max_wind = 200.
    u[np.where(u>max_wind)] = max_wind
    u[np.where(u<-max_wind)] = -max_wind
    v[np.where(v>max_wind)] = max_wind
    v[np.where(v<-max_wind)] = -max_wind

    # this creates the solution container
    sol = Variables(sg)
    sol.h[...] = height.T
    sol.u[...] = u.T
    sol.v[...] = v.T
    sol.F = F.T

    return sol