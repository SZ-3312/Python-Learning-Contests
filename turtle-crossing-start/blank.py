# a = "HURRICANES HENRI AND IDA CAUSED HAVOC FOR MANY"
# c = ""
# for x in range(0, len(a)):
#     b = 0
#     for y in range (0, len(a)):
#         if a[x] == a[y] and x != y:
#             b += 1
#     if b == 0:
#         c += a[x]
#
# if __name__ == '__main__':
#     print(c)

def count_cycles(graph):
    counted = []
    cycles = 0
    for path in graph:
        test = f"{path[1]}{path[0]}"
        if path in counted:
            pass
        elif path[0] == path[1]:
            cycles += 1
        elif test in graph:
            cycles += 1
            counted.append(test)

    return cycles


def count_edges(graph):
    vertex = 0
    edge_map = {}
    list_a = []
    list_b = []
    key_list = []
    for edge in graph:
        key = edge[0]
        if key in edge_map:
            edge_map[key].append(edge)
        else:
            vertex += 1
            key_list.append(key)
            edge_map[key] = [edge]

    for i in range(0, vertex):
        v = key_list[i]
        list_a.append(len(edge_map[str(v)]))
        list_b.append(v)

    m = max(list_a)
    for item in list_a:
        if item == m:
            new_list = []
            m_index = list_a.index(m)
            for v in edge_map[str(list_b[m_index])]:
                new_list.append(int(v))
            output = sum(new_list)
            return output


def main_func(string):
    function_input = string.split(" ")
    direction = function_input[0]
    function_input.pop(0)

    if direction == "1":
        return count_cycles(function_input)
    elif direction == "2":
        return count_edges(function_input)


if __name__ == '__main__':
    print(main_func("2 12 13 23 31 34 41"))
    # Test 0: 2 12 13 23 31 34 41
    # Output: 25
    # Test 1: 1 12 23 34 11 21 32 45 53 95 43 99 29 91
    # Output: 5
    # Test 2: 3 12 23 34 41 31 52 45 61 14 21 33 55 13 54 32 56 36
    # Output: 49
    # Test 3: 1 12 11 33 34 43 55 52 41 31 25 88 79 98 45 13 42 87 35 51 21 14 78
    # Output: 10
    # Test 4: 2 12 11 33 34 43 55 52 41 31 25 88 79 98 45 13 42 87 35 51 21 14 78
    # Output: 50
