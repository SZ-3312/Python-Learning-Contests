# RECURSIVE FUNCTIONS!

# Function #1
def g(x):
    if x > 0:
        return g(x - 3) + 1
    return 3 * x


# Function #2
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# Function #3
def h(x):
    if x > 5:
        return h(x - 7) + 1
    if x < 0:
        return h(x + 3)
    return x


# Function #4
def k(a):
    if a < 1:
        return k(a + 1) * 10
    return a


# Function #5
def f(x):
    if x % 3 == 0 and x % 2 == 1:
        return 2 * f(x / 3) - 1
    elif x % 2 == 0:
        return -1 * f(x / 2) + 2
    return x + 4


# Function #6
def c(x):
    if x > 10:
        return 2 * c(x - 3) - 1
    if x < 2:
        return 3 ** x * x ** 3
    return c(x - 2) + 3


# Function #7
def z(x, y):
    if x > y:
        return z(x - 3, y + 1) + 3
    if x == y:
        return 2 * z(x + 2, y - 3) - 1
    if x < y:
        return x + y


# Function #8
def q(n):
    if n == 1:
        return [0]

    v = q(n - 1)
    v.append(n - 1)
    return v


# Fibonacci Sequence
empty_dict = {}


def fibonacci(n, cache):
    if n in cache:
        return cache[n]

    if n == 1:
        return 1
    if n == 0:
        return 0

    v = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    cache[n] = v
    return v
