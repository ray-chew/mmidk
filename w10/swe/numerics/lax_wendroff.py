import numpy as np


def lax_wendroff(sol, tg, sg, ud):
    # We want the quantities that we are updating with the RLW method
    h = sol.h
    hu = sol.h * sol.u
    hv = sol.h * sol.v

    # Now we need the to specify how we index our arrays.

    # we take the values on the right in the x direction
    r_i = (..., slice(1,None)) 
    # we take the values on the left in the x direction
    l_i = (..., slice(0,-1))
    # we take the values on the right in the y direction
    r_j = (slice(1,None),)
    # we take the values on the left in the y direction
    l_j = (slice(0,-1),)

    # define the inner domain, i.e. without the ghost cells,
    i1 = (slice(1,-1), slice(1,-1))
    in_i = (slice(1,-1),)
    in_j = (..., slice(1,-1))

    # Get values defined by the user in the initial conditions file
    g = ud.g
    f = sol.F[i1]


    # implement substep (2)
    h_ih_nph = 0.5 * (h[r_i] + h[l_i]) - tg.dt / (2.0 * sg.dx) * (hu[r_i] - hu[l_i])

    h_jh_nph = 0.5 * (h[r_j] + h[l_j]) - tg.dt / (2.0 * sg.dy) * (hv[r_j] - hv[l_j])

    hu_flx_i = (hu) * sol.u + g / 2.0 * h**2
    hu_ih_nph = 0.5 * (hu[r_i] + hu[l_i]) - tg.dt / (2.0 * sg.dx) * (hu_flx_i[r_i] - hu_flx_i[l_i])

    hu_flx_j = hv * sol.u
    hu_jh_nph = 0.5 * (hu[r_j] + hu[l_j]) - tg.dt / (2.0 * sg.dy) * (hu_flx_j[r_j] - hu_flx_j[l_j])

    hv_flx_i = hu * sol.v
    hv_ih_nph = 0.5 * (hv[r_i] + hv[l_i]) - tg.dt / (2.0 * sg.dx) * (hv_flx_i[r_i] - hv_flx_i[l_i])

    hv_flx_j = (hv) * sol.v + g / 2.0 * h**2
    hv_jh_nph = 0.5 * (hv[r_j] + hv[l_j]) - tg.dt / (2.0 * sg.dy) * (hv_flx_j[r_j] - hv_flx_j[l_j])


    # implement substep (3)
    h_np1 = h[i1] - tg.dt / sg.dx * (hu_ih_nph[r_i][in_i] - hu_ih_nph[l_i][in_i]) - tg.dt / sg.dy * (hv_jh_nph[r_j][in_j] - hv_jh_nph[l_j][in_j])

    # implement source term for Coriolis parameter
    fvh = f * sol.v[i1] * (h_np1 + h[i1]) / 2.0
    hu_flx_x = hu_ih_nph**2 / h_ih_nph + g / 2.0 * h_ih_nph**2
    hu_flx_y = hu_jh_nph * hv_jh_nph / h_jh_nph
    hu_np1 = hu[i1] - tg.dt / sg.dx * (hu_flx_x[r_i][in_i] - hu_flx_x[l_i][in_i]) - tg.dt / sg.dy * (hu_flx_y[r_j][in_j] - hu_flx_y[l_j][in_j]) + tg.dt * fvh

    fuh = -f * sol.u[i1] * (h_np1 + h[i1]) / 2.0
    hv_flx_x = hu_ih_nph * hv_ih_nph / h_ih_nph
    hv_flx_y = hv_jh_nph**2 / h_jh_nph + g / 2.0 * h_jh_nph**2
    hv_np1 = hv[i1] - tg.dt / sg.dx * (hv_flx_x[r_i][in_i] - hv_flx_x[l_i][in_i]) - tg.dt / sg.dy * (hv_flx_y[r_j][in_j] - hv_flx_y[l_j][in_j]) + tg.dt * fuh

    u_np1 = hu_np1 / h_np1
    v_np1 = hv_np1 / h_np1

    sol.h[i1] = h_np1
    sol.u[i1] = u_np1
    sol.v[i1] = v_np1