# 3rd test (edited)
pascal_map = {}


def fib_index(fib_num):
    count = 1
    prev1 = 1
    prev2 = 1

    while fib_num > prev2:
        count += 1
        new_fib = prev1 + prev2
        if new_fib == fib_num:
            return count
        elif new_fib > fib_num:
            return -1

        prev1 = prev2
        prev2 = new_fib

    return 1


def calculate(r, c):
    if r < 0:
        return -1
    if c == 0:
        return 1
    if c == r:
        return 1
    key = f"{r}, {c}"
    if key in pascal_map:
        return pascal_map[key]
    value = calculate(r - 1, c - 1) + calculate(r - 1, c)
    pascal_map[key] = value
    return value


def print_numbers(fib_number):
    row = fib_index(fib_number)
    column = 0
    total = 0
    solutions = []

    while True:
        number = calculate(row, column)
        if number < 0:
            solutions.append("None\nThe input was not a Fibonacci number.")
            break

        solutions.append(str(number))
        total += number
        if total >= fib_number:
            break

        row -= 1
        column += 1

    return ' '.join(solutions)


if __name__ == '__main__':
    print(print_numbers(280571172992510140037611932413038677189525))
