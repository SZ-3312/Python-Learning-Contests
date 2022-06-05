# FIRST PROGRAMMING PROBLEM FROM CONTEST 2!
def connect(string):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
               "w", "x", "y", "z"]

    for i in range(len(string) - 1, -1, -1):
        if string[i] not in letters:
            string.pop(i)

    return string


def arrange(string):
    distinct_letters = []
    used_letters = []
    while len(string) > 0:
        for i in range(len(string)):
            if string[i] not in distinct_letters:
                distinct_letters.append(string[i])

        distinct_letters = sorted(distinct_letters)

        for i in range(len(distinct_letters)):
            string.remove(distinct_letters[i])

        used_letters.extend(distinct_letters)
        distinct_letters.clear()

    for i in range(len(used_letters) - 1, -1, -1):
        if used_letters[i] == used_letters[i - 1]:
            used_letters.pop(i - 1)

    return ''.join(used_letters)


if __name__ == '__main__':
    value = list(input("Input: ").lower())
    new_str = connect(value)
    print(f"Output: {arrange(new_str)}")
