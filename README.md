# Mathematische Modellierung in der Klimaforschung
This repository contains the course material I created as a voluntary lecturer for the tutorial *Mathematical Modelling in Climate Research* at the Freie Universität Berlin. The `.tex` files used to generate the lecture notes are available upon request.

## Course outline

|  week  | content                                                                       | exercise                                                              | Python crash course              |
|:------:|-------------------------------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------|
|   w0   | an introduction to Git                                                        |                                                                       |                                  |
|   w1   | introduction to numerics with a simple harmonic oscillator                    | Using `scipy.integrate.odeint`                                        | functions and lists              |
|   w2   | discretising the simple harmonic oscillator; numerical stability              | discretising and solving the Lotka-Volterra equations                 | for loops and list comprehension |
|   w3   | order of accuracy and convergence; error analysis                             |                                                                       |                                  |
|   w4   | discretising and solving the heat equation                                    | implement an [FTCS scheme](https://en.wikipedia.org/wiki/FTCS_scheme) | good programming practices       |
|   w5   | [consolidation of knowledge acquired]                                         |                                                                       |                                  |
|   w6   | conservation laws                                                             |                                                                       |                                  |
|   w7   | finite volume method; Burger's equation, Lax-Friedrich, and the CFL condition | discretising and solving the Burgers' equation                        |                                  |
|   w8   | error analysis of the Lax-Friedrich method                                    |                                                                       |                                  |
|   w9   | using a debugger and profiler                                                 | modularising the exercise from w7                                     | classes                          |
|   w10  | shallow water equations; Richtmyer-Lax-Wendroff method                        | [final proj.] implement the discretised shallow water equations       |                                  |
|   w11  | dealing with boundary conditions and source terms                             | [final proj.] implement the discretised shallow water equations       |                                  |
| w12-15 | implement and run the shallow water code; describe the simulation results     | [final proj.] implement the discretised shallow water equations       |                                  |

## License
The material provided in this repository may be freely used, modified, and distributed, subject to an attribution to this repository.

## References
The material from week ten onwards was adapted from [Paul Connolly's webpage](https://personalpages.manchester.ac.uk/staff/paul.connolly/teaching/practicals/shallow_water_equations.html) on the Shallow Water Equations.

The two textbooks I used extensively in preparing these material were Randall J. LeVeque's
  * [Numerical Methods for Conservation Laws](https://link.springer.com/book/10.1007/978-3-0348-8629-1)
  * [Finite Volume Methods for Hyperbolic Problems](https://www.cambridge.org/core/books/finite-volume-methods-for-hyperbolic-problems/97D5D1ACB1926DA1D4D52EAD6909E2B9)

