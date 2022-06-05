def multiply(row, column):
    total = 0
    for i in range(len(row)):
        total += int(row[i]) * int(column[i])
    return str(total)


def square_adj_matrix(rows, columns):
    matrix = []
    paths = 0
    completed_row = ""
    for x in rows:
        for y in columns:
            n = multiply(x, y)
            completed_row += n
            paths += int(n)
            if len(completed_row) == len(rows):
                matrix.append(completed_row + "\n")
                completed_row = ""

    return ''.join(matrix), paths


if __name__ == '__main__':
    r = input("Type in all the rows in the matrix separated by a space: ").split(' ')
    c = []
    new_c = ""
    for z in range(len(r)):
        for original_row in r:
            new_c += original_row[z]
            if len(new_c) == len(original_row):
                c.append(new_c)
                new_c = ""
    final_result, num_of_paths = square_adj_matrix(r, c)
    print(f"\nSquared Result:\n\n{final_result}\nNumber of paths: {num_of_paths}")
