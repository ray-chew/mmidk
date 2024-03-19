import numpy as np

def set_boundary(sol):
    return np.pad(sol.u, (get_ghost(sol.u)), mode='wrap')


def get_ghost(u):
    ghost_cells = [(0,0)]*u.ndim
    ghost_cells[0] = (1,1)
    return ghost_cells
