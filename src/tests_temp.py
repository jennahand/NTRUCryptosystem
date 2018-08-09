from numpy.polynomial import Polynomial

from src.NTRU import N, Q
from src.polynomials import print_polynomial, bytes_to_polynomial, scalar_multiply, generate_random_polynomial, \
    invert, polynomial_multiply, polynomial_add, polynomial_to_bytes, is_invertible, polynomial_degree, \
    truncate_polynomial


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


def test_generate_random_polynomial():
    plaintext = "test"
    message = bytes_to_polynomial(plaintext.encode())
    r = generate_random_polynomial(len(message), 4)
    print_polynomial(r)


def test_is_invertible():
    f = [0] * N
    g = [0] * N
    g[0] = -1
    f[0] = 1
    g[N-1] = 1
    f[1] = 2
    result = is_invertible(f, g, Q, N)
    print(result)


def test_polynomial_multiply():
    f = [0] * N
    g = [0] * (N + 1)
    print(len(f))
    g[0] = -1
    f[0] = 1
    g[N] = 1
    f[1] = 2
    result = polynomial_multiply(f, g, Q, N)
    truncate_polynomial(result)
    print_polynomial(result)


def test_polynomial_add():
    f = [1, 2]
    g = [1, 2]
    result = polynomial_add(f, g, 10)
    print_polynomial(result)


def test_invert():
    N = 11
    q = 32
    f = [-1, 1, 1, 0, -1, 0, 1, 0, 0, 1, -1]
    g = [0] * (N + 1)
    g[N] = 1
    g[0] = -1
    print(invert(f, g, q, N))

test_invert()