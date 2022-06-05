#ACSL FINALS!!!!
def build_list(l, n):
    total_len = int(n * (n + 1) / 2)
    length = len(l)
    new_list = []
    new_list.extend(l)
    while length < total_len:
        length += len(l)
        new_list.extend(l)
    return new_list


def group(l, n):
    l = build_list(l, n)
    index = 0
    gp = []
    while n > 0:
        gp.append(l[index: n + index])
        index += n
        n -= 1
    return gp


def sort_by_int(e):
    return int(e)


def my_sort(g):
    b = False
    for e in g:
        e.sort(reverse=b, key=sort_by_int)
        b = not b


def createWave(waveLength, numbers):
    # Write your code here
    final_wave = ""
    new_numbers = numbers.split(' ')
    groups = group(new_numbers, waveLength)
    my_sort(groups)
    for g in groups:
        final_wave += " ".join(g) + " "
    return ''.join(final_wave)


if __name__ == '__main__':
    print(createWave(6, "3 14 1 59 26 535 8 97 932 38 462 64 3 3 83 279 50 288 4 19 716 939 9 37510"))


