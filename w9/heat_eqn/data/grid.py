import numpy as np

class sGrid(object):
    def __init__(self, ud):
        self.Nx = ud.Nx
        self.xmin = ud.xmin
        self.xmax = ud.xmax

        self.x = np.linspace(self.xmin, self.xmax, self.Nx).reshape(-1,1)
        self.dx = np.diff(self.x.flatten())[0]

        if ud.Ny > 1:
            self.Ny = ud.Ny
            self.ymin = ud.ymin
            self.ymax = ud.ymax

            self.y = np.linspace(self.ymin, self.ymax, self.Ny).reshape(1,-1)
            self.dy = np.diff(self.y.flatten())[0]
        else:
            self.y = 0.0
            self.dy = np.nan

        self.dxy = (self.dx, self.dy)
        self.xg, self.yg = np.meshgrid(self.x, self.y)


class tGrid(object):
    def __init__(self, ud):
        self.T = ud.T
        self.dt = ud.dt
        self.t = np.arange(0.0, self.T+self.dt, self.dt)




