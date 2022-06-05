
def get_next(num, string):
    """Returns the next number greater than the previous number in the input string"""
    index = 1
    while index <= len(string):
        sub = int(string[0:index])
        if sub > int(num):
            return sub, string[index:]
        index += 1
    return -1, "-1"


def order(raw_sequence):
    output = []
    digit = raw_sequence[0]
    result = [digit]
    sequence = raw_sequence[1:]
    digit, sequence = get_next(digit, sequence)

    while digit != -1:
        result.append(digit)
        digit, sequence = get_next(digit, sequence)

    for n in result:
        output.append(str(n))

    return ' '.join(output)


if __name__ == '__main__':
    print(order("19782017"))
