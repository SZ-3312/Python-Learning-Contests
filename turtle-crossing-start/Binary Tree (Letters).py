def compare(a, b):
    if ord(a) >= ord(b):
        return "Left"
    return "Right"


if __name__ == '__main__':
    while True:
        first = input("What is the previous letter?\n")
        if first == 'stop':
            break
        second = input("What is the next letter?\n")
        if second == 'stop':
            break
        print(compare(first[0], second[0]) + '\n')
