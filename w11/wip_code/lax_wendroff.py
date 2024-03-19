import numpy as np


def lax_wendroff(sol, tg, sg, ud):
    # We want the quantities that we are updating with the RLW method
    h = sol.h
    hu = sol.h * sol.u
    hv = sol.h * sol.v

    # Get values defined by the user in the initial conditions file
    g = ud.g

    # Now we need the to specify how we index our arrays.

    # we take the values on the right in the x direction
    r_i = (..., slice(1,None)) 
    # we take the values on the left in the x direction
    l_i = (..., slice(0,-1))
    # we take the values on the right in the y direction
    r_j = (slice(1,None), ...) 
    # we take the values on the left in the y direction
    l_j = (slice(0,-1), ...)


    # implement substep (2)
    h_ih_nph = 0.5 * (h[r_i] + h[l_i]) - tg.dt / (2.0 * sg.dx) * (hu[r_i] - hu[l_i])

    h_jh_nph = 0.5 * (h[r_j] + h[l_j]) - tg.dt / (2.0 * sg.dy) * (hv[r_j] - hv[l_j])

    hu_flx_i = (hu)**2 / h + g / 2.0 * h**2
    hu_ih_nph = 0.5 * (hu[r_i] + hu[l_i]) - tg.dt / (2.0 * sg.dx) * (hu_flx_i[r_i] - hu_flx_i[l_i])

    hu_flx_j = hv * hu / h
    hu_jh_nph = 0.5 * (hu[r_j] + hu[l_j]) - tg.dt / (2.0 * sg.dy) * (hu_flx_j[r_j] - hu_flx_j[l_j])

    hv_flx_i = hu * hv / h
    hv_ih_nph = 0.5 * (hv[r_i] + hv[l_i]) - tg.dt / (2.0 * sg.dx) * (hv_flx_i[r_i] - hv_flx_i[l_i])

    hv_flx_j = (hv)**2 / h + g / 2.0 * h**2
    hv_jh_nph = 0.5 * (hv[r_j] + hv[l_j]) - tg.dt / (2.0 * sg.dy) * (hv_flx_j[r_j] - hv_flx_j[l_j])
 
