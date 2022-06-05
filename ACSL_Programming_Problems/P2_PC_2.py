
equation = ""
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


def left(n, equation):
    passed = False
    solutions = []
    for value in equation:
        if value not in nums:
            solution = equation.index(value) + 1
            if value != n:
                list_equation = list(equation)
                list_equation[solution - 1] = "0"
                equation = ''.join(list_equation)
            if passed and solution > 3 + equation.index(n):
                if solution not in solutions:
                    solutions.append(solution)
            elif value == n:
                passed = True
    solutions.append(len(equation) + 1)

    return solutions


def right(n, equation):
    passed = False
    solutions = [1]
    for value in equation:
        if value not in nums:
            solution = equation.index(value) + 2
            if not passed and solution < equation.index(n) - 1:
                if solution not in solutions:
                    solutions.append(solution)
            elif value == n:
                passed = True

    return solutions


def order(equation):
    if "(" in equation:
        n = "("
        solutions = left(n, equation)
    else:
        n = ")"
        solutions = right(n, equation)
    return solutions


if __name__ == '__main__':
    print(order("9+6)/2–4+5"))

# test case 0: "(2+3*6+1"
# test case 1: "2–5*(6+1"
# test case 2: "5+5–2)*5"
# test case 3: "3*5+(8/4*2"
# test case 4: "2+8/4*5)"
# test case 5: "6+2/3*4)"
# test case 6: "(2–2+2+3*4/2"
# test case 7: "8/(2+3–6+2"
# test case 8: "7–5+8*6/2)+1"
# test case 9: "9+6)/2–4+5"

