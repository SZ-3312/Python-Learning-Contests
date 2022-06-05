# I DID IT!!!!!!!!
def group(string, n):
    start = 0
    end = n
    length = len(string)
    remainder = length % n
    num_of_groups = int((length - remainder)/n)
    if num_of_groups == 0:
        return bin_to_dec(string)

    final_groups = []
    if remainder > 0:
        segment = string[:remainder]
        string = string.removeprefix(segment)
        final_groups.append(segment)

    for i in range(num_of_groups):
        final_groups.append(string[start:end])
        start += n
        end += n

    return final_groups


def bin_to_dec(b):
    output = 0
    dif = 1
    b_list = []

    for item in b:
        b_list.append(item)

    for v in b_list:
        output += int(v) * 2 ** (len(b_list) - dif)
        dif += 1

    return [str(output)]


def bin_to(b, system):
    letters = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }

    final = ""
    if system == "oct":
        bin_list = group(b, 3)
        for value in bin_list:
            val = ''.join(bin_to_dec(value))
            final += val

    elif system == "hex":
        bin_list = group(b, 4)
        for value in bin_list:
            val = ''.join(bin_to_dec(value))
            if val in letters:
                final += letters[val]
            else:
                final += val

    return final


def to_bin(x, system):
    values = {
        "A": "10",
        "B": "11",
        "C": "12",
        "D": "13",
        "E": "14",
        "F": "15",
    }
    output = []
    recursion = 0
    if system == "oct":
        g_len = 3
    else:
        g_len = 4

    for v in x:
        if v in values:
            v = values[v]
        bin_num = str(bin(int(v))).removeprefix("0b")
        output.append(bin_num)

    for item in output:
        difference = g_len - len(item)
        if difference > 0 and recursion > 0:
            new_item = difference * "0" + item
            index = output.index(item)
            output.insert(index, new_item)
            output.pop(index + 1)
        recursion += 1

    return ''.join(output)


def to_dec(v, sys):
    bin_num = to_bin(v, sys)
    return ''.join(bin_to_dec(bin_num))


def switch(n):
    if n == "db":
        msg = input("Decimal -> Binary\n")
        return str(bin(int(msg))).removeprefix("0b")
    elif n == "bd":
        msg = input("Binary -> Decimal\n")
        return ''.join(bin_to_dec(msg))
    elif n == "bo":
        msg = input("Binary -> Octal\n")
        return bin_to(msg, "oct")
    elif n == "ob":
        msg = input("Octal -> Binary\n")
        return to_bin(msg, "oct")
    elif n == "od":
        msg = input("Octal -> Decimal\n")
        return to_dec(msg, "oct")
    elif n == "bh":
        msg = input("Binary -> Hexadecimal\n")
        return bin_to(msg, "hex")
    elif n == "hb":
        msg = input("Hexadecimal -> Binary\n")
        return to_bin(msg, "hex")
    elif n == "hd":
        msg = input("Hexadecimal -> Decimal\n")
        return to_dec(msg, "hex")


if __name__ == '__main__':
    names = {
        "d": "Decimal",
        "b": "Binary",
        "o": "Octal",
        "h": "Hexadecimal",
    }
    prompt = ""
    choices = "od/hd/bd/bo/bh/ob/hb/db".split("/")
    while prompt != "stop":
        prompt = input("od/hd/bd/bo/bh/ob/hb/db\n")
        if prompt in choices:
            final_output = switch(prompt)
            print(f"Result: {final_output} ({names[prompt[1]]})")
        else:
            print("Your input was not valid.")
