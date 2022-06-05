
# Complete the 'findTime' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. CHARACTER c1
#  2. CHARACTER c2
#  3. CHARACTER c3
#  4. CHARACTER c4
#  5. CHARACTER c5


def find_time(c1, c2, c3, c4, c5):
    # Write your code here
    v = [c1, c2, c3, c4, c5]
    fibonacci = [1, 1, 2, 3, 5]
    colors = {
        "R": 0,
        "B": 0,
        "G": 0,
        "W": 0
    }

    for i in range(len(v)):
        colors[v[i]] += fibonacci[i]

    red, blue, green = colors["R"], colors["B"], colors["G"]
    hours = red + blue
    minutes = (green + blue) * 5

    hours = f"0{hours}" if hours < 10 else hours
    minutes = f"0{minutes}" if minutes < 10 else minutes

    time = f"{hours}:{minutes}"
    return time


if __name__ == '__main__':
    result = find_time("R", "R", "R", "R", "R")
    print(result + '\n')
