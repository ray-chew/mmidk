from data.grid import sGrid, tGrid
from numerics.lax_wendroff import lax_wendroff
from numerics.bc import set_boundary
from data import io

import numpy as np

if __name__ == '__main__':
    user_data, sol_init = io.get_args()
    ud = user_data()

    writer = io.writer(filename=ud.fn)

    sg = sGrid(ud)
    tg = tGrid(ud)
    writer.write_attr(ud)
    writer.write_attr(sg)
    writer.write_attr(tg)

    sol = sol_init(sg, ud)
    writer.write(0, 'H', sol.H)
    writer.write(0, 'F', sol.F)

    for nn, tt in enumerate(tg.t):

        if tt % ud.output_interval == 0:
            max_u = np.sqrt(np.max(sol.u**2 + sol.v**2))
            print("Time = %f hours (max %f); max(|u|) = %f" % ((tt)/3600., tg.t[-1] / 3600, max_u) )
            writer.write(nn, 'h', sol.h)
            writer.write(nn, 'u', sol.u)
            writer.write(nn, 'v', sol.v)

        lax_wendroff(sol, tg, sg, ud)
        set_boundary(sol)








