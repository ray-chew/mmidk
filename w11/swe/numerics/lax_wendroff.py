import numpy as np

from copy import deepcopy

def lax_wendroff(sol, tg, sg, ud):
    li, ri = (...,slice(0,-1)), (...,slice(1,None))
    lj, rj = (slice(0,-1),), (slice(1,None),) 
    i1, i1i, i1j = (slice(1,-1),slice(1,-1)), (...,slice(1,-1)), (slice(1,-1),)

    hu = sol.h * sol.u
    hv = sol.h * sol.v

    #####

    hi_nph = 0.5 * (sol.h[li] + sol.h[ri]) - tg.dt / (2.0 * sg.dx) * (hu[ri] - hu[li])
    hj_nph = 0.5 * (sol.h[lj] + sol.h[rj]) - tg.dt / (2.0 * sg.dy) * (hv[rj] - hv[lj])

    hui_flx = hu*sol.u + ud.g / 2.0 * sol.h**2
    hui_nph = 0.5 * (hu[li] + hu[ri]) - tg.dt / (2.0 * sg.dx) * (hui_flx[ri] - hui_flx[li])

    huj_flx = hu*sol.v
    huj_nph = 0.5 * (hu[lj] + hu[rj]) - tg.dt / (2.0 * sg.dy) * (huj_flx[rj] - huj_flx[lj])

    hvi_flx = hu*sol.v
    hvi_nph = 0.5 * (hv[li] + hv[ri]) - tg.dt / (2.0 * sg.dx) * (hvi_flx[ri] - hvi_flx[li])

    hvj_flx = hv*sol.v + ud.g / 2.0 * sol.h**2
    hvj_nph = 0.5 * (hv[lj] + hv[rj]) - tg.dt / (2.0 * sg.dy) * (hvj_flx[rj] - hvj_flx[lj])

    #####

    uF =  sol.F[i1] * sol.v[i1]
    vF = -sol.F[i1] * sol.u[i1]

    h_np1 = sol.h[i1] - (tg.dt / sg.dx) * (hui_nph[ri][i1j] - hui_nph[li][i1j]) - (tg.dt / sg.dy) * (hvj_nph[rj][i1i] - hvj_nph[lj][i1i])

    hui_flx_nph = hui_nph**2 / hi_nph + ud.g / 2.0 * hi_nph**2
    huj_flx_nph = huj_nph * hvj_nph / hj_nph
    hu_np1 = hu[i1] - (tg.dt / sg.dx) * (hui_flx_nph[ri][i1j] - hui_flx_nph[li][i1j]) - (tg.dt / sg.dy) * (huj_flx_nph[rj][i1i] - huj_flx_nph[lj][i1i]) + tg.dt * uF * (sol.h[i1] + h_np1) / 2.0 

    hvi_flx_nph = hui_nph * hvi_nph / hi_nph
    hvj_flx_nph = hvj_nph**2 / hj_nph + ud.g / 2.0 * hj_nph**2
    hv_np1 = hv[i1] - (tg.dt / sg.dx) * (hvi_flx_nph[ri][i1j] - hvi_flx_nph[li][i1j]) - (tg.dt / sg.dy) * (hvj_flx_nph[rj][i1i] - hvj_flx_nph[lj][i1i]) + tg.dt * vF * (sol.h[i1] + h_np1) / 2.0 

    sol.h[i1] = h_np1
    sol.u[i1] = hu_np1 / h_np1
    sol.v[i1] = hv_np1 / h_np1