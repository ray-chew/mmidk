import numpy as np

def set_boundary(sol):
    # we set periodic BC in the x-direction
    sol.h[:,0] = sol.h[:,-2]
    sol.h[:,-1] = sol.h[:,1]

    sol.u[:,0] = sol.u[:,-2]
    sol.u[:,-1] = sol.u[:,1]

    sol.v[:,0] = sol.v[:,-2]
    sol.v[:,-1] = sol.v[:,1]

    # we set no-flux BC in the y-direction
    sol.v[[0,-1],:] = 0.0

    # sol.h[0,:] = sol.h[-2,:]
    # sol.h[-1,:] = sol.h[1,:]

    # sol.u[0,:] = sol.u[-2,:]
    # sol.u[-1,:] = sol.u[1,:]

    # sol.v[0,:] = sol.v[-2,:]
    # sol.v[-1,:] = sol.v[1,:]

