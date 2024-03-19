import numpy as np

def set_boundary(sol):
    i1i = (..., slice(1,-1))
    i1j = (slice(1,-1),...)
    # sol.h[...] = np.pad(sol.h[i1i], (get_ghost(sol.h, 1)), mode='wrap')
    # sol.u[...] = np.pad(sol.u[i1i], (get_ghost(sol.u, 1)), mode='wrap')
    # sol.v[...] = np.pad(sol.v[i1i], (get_ghost(sol.v, 1)), mode='wrap')


    # sol.h[...] = np.pad(sol.h[i1j], (get_ghost(sol.h, 0)), mode='symmetric')
    # sol.u[...] = np.pad(sol.u[i1j], (get_ghost(sol.u, 0)), mode='symmetric')
    # sol.v[...] = np.pad(sol.v[i1j], (get_ghost(sol.v, 0)), mode='symmetric')

    sol.h[:,-1] = sol.h[:,1]
    sol.u[:,-1] = sol.u[:,1]
    sol.v[:,-1] = sol.v[:,1]

    sol.h[:,0] = sol.h[:,-2]
    sol.u[:,0] = sol.u[:,-2]
    sol.v[:,0] = sol.v[:,-2]

    sol.v[[0,-1],:] = 0.0

def get_ghost(u, idx):
    ghost_cells = [(0,0)]*u.ndim
    ghost_cells[idx] = (1,1)
    return ghost_cells
