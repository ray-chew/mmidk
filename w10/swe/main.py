from data.grid import sGrid, tGrid
from numerics.lax_wendroff import lax_wendroff
from numerics.bc import set_boundary
from data import io


if __name__ == '__main__':
    user_data, sol_init = io.get_args()
    ud = user_data()

    writer = io.writer()

    sg = sGrid(ud)
    tg = tGrid(ud)
    writer.write_attr(sg)
    writer.write_attr(tg)

    sol = sol_init(sg,ud)

    for nn, t in enumerate(tg.t):

        if nn % 60 == 0:
            writer.write(nn, "h", sol.h)
            writer.write(nn, "u", sol.u)
            writer.write(nn, "v", sol.v)
            print("time-step %.2f" %nn)

        lax_wendroff(sol, tg, sg, ud)
        set_boundary(sol)







