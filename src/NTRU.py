from numpy.polynomial.polynomial import polyzero

from src.polynomials import is_invertible, generate_random_polynomial, scalar_multiply, polynomial_multiply, \
    polynomial_add, bytes_to_polynomial
from src.polynomials import invert


# Parameters
N = 659

P = 3

Q = 2039

D_G = N / 3

D = 38


def generate_keys():
    f_prime = generate_random_polynomial(N, D)
    g_prime = generate_random_polynomial(N, D)

    f = polynomial_multiply([P], f_prime, Q)
    f[0] = f[0] + 1

    # while not is_invertible(f, Q):
    #     f_prime = generate_random_polynomial(N, D)
    #     f = polynomial_multiply([P], f_prime, Q)
    #     f[0] = f[0] + 1


    g = scalar_multiply(P, g_prime, Q)
    # while not is_invertible(g, Q):
    #     g_prime = generate_random_polynomial(N, D)
    #     g = scalar_multiply(P, g_prime, Q)

    #h = invert(f, Q) * g
    return f, h


def encrypt(m):
    m_poly = bytes_to_polynomial(m, N)
    f, h = generate_keys()
    r = generate_random_polynomial(N)
    hr = polynomial_multiply(h, r, Q)
    return f, polynomial_add(m_poly, hr, Q)


def decrypt(f, c):
    a = polynomial_multiply(f, c, Q)
    #TODO: centered coefficients
    return polynomial_add(a, polyzero, P)

