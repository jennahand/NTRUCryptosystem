from src.NTRU import N, Q
from src.polynomials import polynomial_print, bytes_to_polynomial, polynomial_scalar_multiply, \
    polynomial_generate_random, \
    polynomial_invert, polynomial_multiply, polynomial_add, polynomial_to_bytes, \
    mod_inverse, polynomial_subtract, polynomial_pad, polynomial_shift, \
    polynomial_divide, polynomial_mod_coefficients, polynomial_degree


# def string_to_byte_array():
#     message = "1"
#     bytes = bytearray(message.encode())
#     print(message.encode())
#     for byte in bytes:
#         print(byte)
#     for byte in bytes:
#         for i in range(0, 8):
#             print(byte & 1)
#             byte = byte >> 1
#
#
# def print_binary():
#     message = int('0x1', 16);
#     print(message)
#     bytes = message.to_bytes(1, byteorder='big')
#     # for byte in bytes:
#     #     print(byte)
#     for byte in bytes:
#         for i in range(0, 8):
#             print(byte & 1)
#             byte = byte >> 1


def test_bytes_to_polynomial(m):
    poly = bytes_to_polynomial(bytearray(m.encode()), N)
    test = polynomial_to_bytes(poly)
    return m == test


def test_polynomial_to_bytes():
    m = "hey there"
    m_bytes = bytearray(m.encode())
    for byte in m_bytes:
        print(byte), print(' '),
    poly = bytes_to_polynomial(m_bytes, N)
    polynomial_print(poly)

    new_bytes = polynomial_to_bytes(poly)
    for byte in new_bytes:
        print(byte), print(' ')
    for byte in new_bytes:
        print(chr(byte))


def test_generate_random_polynomial():
    plaintext = "test"
    message = bytes_to_polynomial(plaintext.encode())
    r = polynomial_generate_random(len(message), 4)
    polynomial_print(r)


def test_polynomial_multiply():
    f = [0] * N
    g = [0] * N
    f[0] = 1
    f[1] = 1
    g[0] = 1
    g[1] = 1
    result = polynomial_multiply(g, f, Q, N)
    polynomial_print(result)


def test_polynomial_add():
    f = [3, 4]
    g = [1, 2]
    result = polynomial_add(f, g)
    polynomial_print(result)


def test_pad_polynomial():
    f = [3, 4]
    f = polynomial_pad(f, 4)
    polynomial_print(f)


def test_polynomial_subtract():
    f = [3, 4]
    g = [1, 2]
    result = polynomial_subtract(f, g)
    polynomial_print(result)


def test_invert():
    N = 11
    q = 32
    f = [-1, 1, 1, 0, -1, 0, 1, 0, 0, 1, -1, 0]
    g = [0] * (N + 1)
    g[N] = 1
    g[0] = -1
    print(polynomial_invert(f, g, q, N))


def test_mod_inverse():
    f = 3
    g = 26
    print(mod_inverse(f, g))


def test_polynomial_shift():
    f = [1, 1, 1, 0, 0]
    f = polynomial_shift(f, 2)
    f = polynomial_scalar_multiply(2, f)
    polynomial_print(f)


def test_polynomial_divide():
    f = [0] * N
    g = [0] * N
    f[0] = -42
    f[1] = 0
    f[2] = -12
    f[3] = 1
    g[0] = -3
    g[1] = 1
    q, r = polynomial_divide(f, g, N)
    polynomial_print(q)
    polynomial_print(r)


def test_polynomial_make_positive():
    f = [-1, 1, -1, 2]
    polynomial_print(f)
    f = polynomial_mod_coefficients(f, Q)
    polynomial_print(f)


def test_polynomial_degree():
    f = [0] * N
    f[0] = 1
    f[4] = 1
    print(polynomial_degree(f))

    g = [0] * N
    print(polynomial_degree(g))


def test_g_polynomial():

    g = polynomial_generate_random(32, 32//3)
    neg_sum = 0
    pos_sum = 0
    for co in g:
        if co < 0:
            neg_sum += 1
        if co > 0:
            pos_sum += 1
    print(neg_sum)
    print(pos_sum)
    polynomial_print(g)


def thing():
    print(mod_inverse(1, Q))

test_polynomial_divide()