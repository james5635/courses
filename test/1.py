import sympy 
from sympy import symbols, Symbol, init_printing
from sympy.solvers import solve
init_printing()
x: int = Symbol(r'\alpha_i')
x
u = symbols('alpha b')
[print(x) for x in u]
eq = 875 - 50 * x

solution = solve(eq,x)
print("x = ", solution[0])