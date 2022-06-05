# FINAL CONTEST :)
from math import sqrt


def square(real, imag):
    x = real
    y = imag
    result_r = (x ** 2) - (y ** 2)
    result_i = (x * y * 2)
    return result_r, result_i


def absolute(real, imag):
    return sqrt(real ** 2 + imag ** 2)


def add(real1, imag1, real2, imag2):
    return real1 + real2, imag1 + imag2


def recursive(real, imag, o_real, o_imag, iteration):
    i = iteration
    if absolute(real, imag) > 4:
        return f"ESCAPES {iteration}"
    if iteration == 5:
        return round(absolute(real, imag), 3)
    i += 1
    sqr, sqi = square(real, imag)
    f1, f2 = add(sqr, sqi, o_real, o_imag)
    return recursive(f1, f2, o_real, o_imag, i)


def abs_result(real_partk, imag_partk):
    o_real = real_partk
    o_imag = imag_partk
    final = str(recursive(0, 0, o_real, o_imag, 0))

    if len(final) < 5:
        for i in range(0, 5 - len(final)):
            final += "0"
    return final


if __name__ == "__main__":
    print(abs_result(0, 0))
