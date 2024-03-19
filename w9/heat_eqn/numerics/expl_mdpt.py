import numpy as np
from numerics.ctr_diff import rhs
from tqdm import tqdm


def time_update(sol, tg, sg, writer):
    for time in tqdm(tg.t):
        u0 = np.copy(sol.u)
        sol.u[...] = u0 + 0.5 * tg.dt * rhs(sol, sg.dxy)
        sol.u[...] = u0 + tg.dt * rhs(sol, sg.dxy)

        writer.write(time, 'u', sol.u)