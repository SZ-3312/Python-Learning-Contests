#YAY :)

def num_of_digits(n):
    return len(str(n))


def sum_of_all_digits(n):
    b_total = 0
    b = str(n)
    b_index = 0
    for i in range(len(b)):
        b_total += int(b[b_index])
        b_index += 1

    return b_total


def sum_of_odd_digits(n):
    c_total = 0
    c = str(n)
    c_index = 0
    while True:
        c_total += int(c[c_index])
        if c_index + 2 < len(c):
            c_index += 2
        else:
            break
    return c_total


def count(n, x):
    d = str(n)
    d_index = 0
    amount = 0
    for i in range(len(d)):
        if str(x) == d[d_index]:
            amount += 1
        d_index += 1
    return amount


def middle_digit(n):
    e = str(n)
    length = len(e)
    if length % 2 == 0:
        mid_pos = int(length / 2)
        mid_dig = e[mid_pos - 1]
    else:
        mid_dig = e[int(length / 2)]
    return mid_dig


def calculate(p):
    func_map = {
        "num_of_digits": num_of_digits,
        "sum_of_all_digits": sum_of_all_digits,
        "sum_of_odd_digits": sum_of_odd_digits,
        "count": count,
        "middle_digit": middle_digit
    }

    if len(p) == 2:
        return func_map[p[0]](p[1])
    elif len(p) == 3:
        return func_map[p[0]](p[1], p[2])


def main():
    input_nums = [
        ("num_of_digits", 1325678945),
        ("sum_of_all_digits", 987654),
        ("sum_of_odd_digits", 456160),
        ("count", 143295823976154, 4),
        ("middle_digit", 123456)
    ]

    for i in input_nums:
        print(calculate(i))


if __name__ == "__main__":
    main()