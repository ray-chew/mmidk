import numpy as np
from numerics.bc import set_boundary

def rhs(sol, dxy):
    sol.fu[...] = 0.0

    for dim in range(sol.u.ndim):
        u = set_boundary(sol)
        lu = u[:-2,...]
        ru = u[2:,...]
        cu = u[1:-1,...]

        sol.fu += (lu - 2.0*cu + ru) / dxy[dim]**2
        sol.flip()

    return sol.fu

