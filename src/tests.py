from src.polynomials import print_polynomial, mod_polynomial, polynomial_degree, mod_coefficients

a = [1, 4, 1, 3, 0]
m = [1, 0, 0, 1, 0]

print(polynomial_degree(a))
print(polynomial_degree(m))

print_polynomial(a)
print_polynomial(m)

a = mod_polynomial(a, m)
print_polynomial(a)
a = mod_coefficients(a, 3)
print_polynomial(a)