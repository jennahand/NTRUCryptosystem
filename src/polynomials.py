import random
from numpy.polynomial.polynomial import polydiv, polysub, polyadd


def generate_random_polynomial(length, d):
    # polynomial with all coefficients initialized to zero
    polynomial = [0] * length

    # collect d + d random indices for 1 and -1 coefficients
    d_indices = set()
    while len(d_indices) < d * 2:
        d_indices.add(random.randint(0, length - 1))

    d_indices = list(d_indices)
    random.shuffle(d_indices)

    # set first half of random indices to 1
    for i in range(0, d):
        polynomial[d_indices[i]] = 1

    # set second half of random indices to -1
    for i in range(d, 2 * d):
        polynomial[d_indices[i]] = -1

    return polynomial


def bytes_to_polynomial(data, length):
    polynomial = [0] * length
    j = 0
    for byte in data:
        for i in range(0, 8):
            polynomial[j + i] = byte & 1
            byte = byte >> 1
        j += 8
    return polynomial


def polynomial_to_bytes(poly):
    byte_values = []
    truncate_polynomial(poly)
    i = 0
    while i < len(poly):
        byte_value = 0
        for j in range(0, 8):
            if i + j < len(poly):
                byte_value += poly[i+j] * pow(2, j)
        byte_values.insert(i//8, byte_value)
        i += 8

    return byte_values


def pad_polynomial(f, n):
    result = f.copy()
    for i in range(len(f), n):
        result.append(0)
    return result


def truncate_polynomial(poly):
    i = len(poly)
    leading_bit = poly[i - 1]
    while leading_bit == 0:
        poly.pop()
        i -= 1
        leading_bit = poly[i - 1]


def scalar_multiply(scalar, polynomial, mod):
    for i in range(0, len(polynomial)):
        polynomial[i] *= scalar % mod


def kth_product_element(f, g, k):
    k_sum = 0
    for i in range(0, len(f)):
        k_sum += f[i] * g[k - i]
    return k_sum


# multiplies polynomials
def polynomial_multiply(f, g, q, N):
    result = []
    for k in range(0, N):
        result.append(kth_product_element(f, g, k))
    return result


# adds polynomials
def polynomial_add(f, g):
    result = [0] * len(f)
    for i in range(0, len(result)):
        result[i] = f[i] + g[i]
    return result


# subtracts polynomials
def polynomial_subtract(f, g):
    result = [0] * len(f)
    for i in range(0, len(result)):
        result[i] = f[i] - g[i]
    return result


# mods coefficients of a polynomial f by modulus m
def mod_coefficients(f, m):
    for i in range(0, len(f)):
        f[i] = f[i] % m
    return f


# mods polynomial f by polynomial m
def mod_polynomial(f, m):
    result = f.copy()
    while polynomial_degree(f) >= polynomial_degree(m):
        result = polysub(result, m)
    return result


def center_coefficients(f, q):
    result = f.copy()
    for i in range(0, len(f)):
        if result[i] > (q - 1)//2:
            result[i] = result[i] - q
    return result


def polynomial_degree(f):
    i = len(f) - 1
    leading_co = f[i]
    while leading_co == 0:
        i -= 1
        leading_co = f[i]
    return i


def is_invertible(f, g, q, N):
    inverse = invert(f, g, q, N)
    if type(inverse) == list:
        return True
    return inverse


# extended euclidean algorithm
def invert(f, g, q, N):
    F = f
    G = g

    B = [0] * N
    B[0] = 1
    C = [0] * N

    while polynomial_degree(F) > 0:
        # swap f and g
        f_temp = F
        F = G
        G = f_temp

        # swap b and c
        b_temp = B
        B = C
        C = b_temp

        f_degree = polynomial_degree(F)
        g_degree = polynomial_degree(G)
        while f_degree >= g_degree:
            j = f_degree - g_degree
            h_scalar = F[f_degree] * mod_inverse(G[g_degree], q)

            H = [0] * N
            H[j] = h_scalar
            print_polynomial(F)

            F = polynomial_subtract(F, polynomial_multiply(H, G, q, N), q)
            print_polynomial(F)
            B = polynomial_subtract(B, polynomial_multiply(H, C, q, N), q)

            f_degree = polynomial_degree(F)
            g_degree = polynomial_degree(G)

    if polynomial_degree(F) > 0:
        return scalar_multiply(mod_inverse(F[0], q), B, q)
    else:
        return False


def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algorithm
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if x < 0:
        x = x + m0

    return x


def print_polynomial(poly):
    i = 0
    output = list()
    for coefficient in poly:
        output.append(str(coefficient) + "x^" + str(i) + " + ")
        i = i + 1
    s = ''.join(output)
    s = s[:-2]
    print(s)
