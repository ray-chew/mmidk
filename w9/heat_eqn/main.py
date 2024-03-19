from data.grid import sGrid, tGrid
from numerics.expl_mdpt import time_update
from data import io


if __name__ == '__main__':
    user_data, sol_init = io.get_args()
    ud = user_data()

    writer = io.writer()

    sg = sGrid(ud)
    tg = tGrid(ud)
    writer.write_attr(sg)
    writer.write_attr(tg)

    sol = sol_init(sg)

    time_update(sol, tg, sg, writer)



