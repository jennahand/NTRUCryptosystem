import random


# polynomial module provides operations on array/vector representations of
# polynomials in a finite ring
# ex: x^3 + 2x + 1 is represented at [1, 2, 0, 1]


# generates a random polynomial of specified possible length where
# d coefficents are 1, d coefficients are -1, and all others are zero
def polynomial_generate_random(length, d):
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

    # set sec ond half of random indices to -1
    for i in range(d, 2 * d):
        polynomial[d_indices[i]] = -1

    return polynomial


#TODO: test
# string to byte array to polynomial
def string_to_polynomial(data, lenght):
    bytes = bytearray(data)
    return bytes_to_polynomial(bytes, length(bytes))


# TODO: test
# polynomial to string
def polynomial_to_string(poly):
    bytes = polynomial_to_bytes(poly)
    result = "".join(map(chr, bytes))
    return result


# byte array to polynomial
def bytes_to_polynomial(bytes, length):
    polynomial = [0] * length
    j = 0
    for byte in bytes:
        for i in range(0, 8):
            polynomial[j + i] = byte & 1
            byte = byte >> 1
        j += 8
    return polynomial


# polynomial to byte array
def polynomial_to_bytes(poly):
    byte_values = []
    polynomial_truncate(poly)
    i = 0
    while i < len(poly):
        byte_value = 0
        for j in range(0, 8):
            if i + j < len(poly):
                byte_value += poly[i + j] * pow(2, j)
        byte_values.insert(i // 8, byte_value)
        i += 8

    return byte_values


# adds leading zeroes to polynomial f such that it is length n
def polynomial_pad(f, n):
    result = f.copy()
    for i in range(len(f), n):
        result.append(0)
    return result


# removes leading zeroes of a polynomial
def polynomial_truncate(poly):
    i = len(poly)
    leading_bit = poly[i - 1]
    while leading_bit == 0:
        poly.pop()
        i -= 1
        leading_bit = poly[i - 1]


# removes leading zeroes of a polynomial to a certain length
def polynomial_truncate_length(poly, n):
    for i in range(n, len(poly)):
        poly.pop()


# polynomial scalar multiplication
def polynomial_scalar_multiply(scalar, f):
    result = f.copy()
    for i in range(0, len(result)):
        result[i] *= scalar
    return result


# multiplies polynomials by convolution
def polynomial_multiply(f, g, q, N):
    result = []
    for k in range(0, N):
        result.append(kth_product_element(f, g, k, q, N) % q)
    return result


def kth_product_element(f, g, k, q, N):
    k_sum = 0
    for i in range(0, N):
        k_sum += (q + f[i]) * (q + g[k - i])
    return k_sum


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


# # polynomial division algorithm
# def polynomial_divide(f, g, N):
#     degree_g = polynomial_degree(g)
#     if degree_g < 0:
#         return
#     F = f.copy()
#     q = [0] * N
#     degree_f = polynomial_degree(F)
#     while degree_f >= degree_g:
#         d = polynomial_shift(g, degree_f - degree_g)
#         q[degree_f - degree_g] = F[degree_f] // d[polynomial_degree(d)]
#         d = polynomial_scalar_multiply(q[degree_f - degree_g], d)
#         F = polynomial_subtract(F, d)
#         degree_f = polynomial_degree(F)
#     r = F
#     return q, r


def polynomial_divide(a, b, Q, N):
    if polynomial_is_zero(a) or polynomial_is_zero(b):
        raise Exception("Zero has no multiplicative inverse!")
    q = [0] * N
    r = a
    d = polynomial_degree(b)
    c = b[d]
    degree_r = polynomial_degree(r)
    while degree_r >= d:
        j = degree_r - d
        s_scalar = r[degree_r] * mod_inverse(c, Q)
        q[j] += s_scalar
        sb = polynomial_scalar_multiply(s_scalar, polynomial_shift(b, j))
        r = polynomial_subtract(r, sb)
        r = polynomial_mod_coefficients(r, Q)
        degree_r = polynomial_degree(r)

    return q, r


# "shifts" a polynomial f to the right i times
def polynomial_shift(f, i):
    result = f.copy()
    for j in range(0, i):
        result.insert(0, 0)
        result.pop()
    return result


# mods coefficients of a polynomial f by modulus m
def polynomial_mod_coefficients(f, m):
    for i in range(0, len(f)):
        f[i] = f[i] % m
    return f


# centers the coefficients of polynomial f in range -(q-1)/2 to (q-1)/2
def polynomial_center_coefficients(f, q):
    result = f.copy()
    for i in range(0, len(f)):
        if result[i] > (q - 1) // 2:
            result[i] = result[i] - q
    return result


# computes the degree of polynomial f
def polynomial_degree(f):
    i = len(f) - 1
    leading_co = f[i]
    while leading_co == 0 and i >= 0:
        i -= 1
        leading_co = f[i]
    return i


# def polynomial_is_invertible(f, g, q, N):
#     inverse = polynomial_invert(f, g, q, N)
#     if type(inverse) == list:
#         return True
#     return inverse


# # extended euclidean algorithm
# # determines the inverse of f mod g
# def polynomial_invert(f, g, q, N):
#     F = f.copy()
#     G = g.copy()
#     # F = polynomial_mod_coefficients(F, q)
#     # G = polynomial_mod_coefficients(G, q)
#     F = polynomial_pad(F, len(g))
#
#     B = [0] * len(g)
#     B[0] = 1
#     C = [0] * len(g)
#
#     while polynomial_degree(F) > 0:
#         # swap f and g
#         f_temp = F
#         F = G
#         G = f_temp
#
#         # swap b and c
#         b_temp = B
#         B = C
#         C = b_temp
#
#         f_degree = polynomial_degree(F)
#         g_degree = polynomial_degree(G)
#         while f_degree >= g_degree:
#             j = f_degree - g_degree
#             h_scalar = F[f_degree] * mod_inverse(G[g_degree], q)
#             HG = polynomial_shift(G, j)
#             HG = polynomial_scalar_multiply(h_scalar, HG)
#
#             HC = polynomial_shift(C, j)
#             HC = polynomial_scalar_multiply(h_scalar, HC)
#
#             F = polynomial_subtract(F, HG)
#             B = polynomial_subtract(B, HC)
#
#             # F = polynomial_mod_coefficients(F, q)
#             # B = polynomial_mod_coefficients(B, q)
#             f_degree = polynomial_degree(F)
#             g_degree = polynomial_degree(G)
#
#     if G[0] > 0:
#         return polynomial_scalar_multiply(mod_inverse(G[0], q), C)
#     else:
#         return False


# adds q to each coefficient of polynomial f
def polynomial_make_positive(f, q):
    result = f.copy()
    for i in range(0, len(result)):
        result[i] = result[i] + q
    return result


# prints a polynomial in the format x^0 + x^1 + ... + x^n
def polynomial_print(poly):
    i = 0
    output = list()
    for coefficient in poly:
        output.append(str(coefficient) + "x^" + str(i) + " + ")
        i = i + 1
    s = ''.join(output)
    s = s[:-2]
    print(s)


# computes the inverse of integer a mod integer m
def mod_inverse(a, m):
    t = 0
    new_t = 1
    r = m
    new_r = a

    while new_r != 0:
        quotient = r // new_r

        temp_t = t
        t = new_t
        new_t = temp_t - (quotient * new_t)

        temp_r = r
        r = new_r
        new_r = temp_r - (quotient * new_r)

    if r > 1:
        return -1
    if t < 0:
        t = t + m
    return t


def polynomial_is_zero(f):
    for co in f:
        if co != 0:
            return False
    return True


# computes the inverse of polynomial a mod polynomial b
def polynomial_gcd(a, b, q, n):
    # check to see if polynomials are padded)
    a = polynomial_mod_coefficients(a, q)
    b = polynomial_mod_coefficients(b, q)
    if len(a) < len(b):
        a = polynomial_pad(a, len(b))
    r_0 = a
    r_1 = b
    s_0 = [0] * len(a)
    s_0[0] = 1
    s_1 = [0] * len(a)
    t_0 = [0] * len(a)
    t_1 = [0] * len(a)
    t_1[0] = 1

    new_r = r_1
    while not polynomial_is_zero(new_r):
        quo, r = polynomial_divide(r_0, r_1, q, len(a))
        quo = polynomial_mod_coefficients(quo, q)

        new_r = polynomial_subtract(r_0, polynomial_multiply(quo, r_1, q, len(a)))
        new_s = polynomial_subtract(s_0, polynomial_multiply(quo, s_1, q, len(a)))
        new_t = polynomial_subtract(t_0, polynomial_multiply(quo, t_1, q, len(a)))

        new_r = polynomial_mod_coefficients(new_r, q)
        new_s = polynomial_mod_coefficients(new_s, q)
        new_t = polynomial_mod_coefficients(new_t, q)

        r_0 = r_1
        s_0 = s_1
        t_0 = t_1

        r_1 = new_r
        s_1 = new_s
        t_1 = new_t

    if r_0[0] == 1:
        polynomial_truncate_length(s_0, n)
        return s_0
    return False
