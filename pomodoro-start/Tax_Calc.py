import math


def calc(amount):
    tax = amount * 0.99
    return amount - round((amount - tax) * 0.99)


if __name__ == '__main__':
    print(calc(244188))
