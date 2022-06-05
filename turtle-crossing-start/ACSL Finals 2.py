
def translate(h, m, s):
    color_map = {
        0: "k",
        1: "b",
        2: "g",
        4: "r",
        3: "y",
        5: "c",
        6: "m",
        7: "w",
    }
    return color_map[h + m + s]


def displayTime(time):
    # Write your code here Red: hours Green: minutes Blue: seconds
    time = time.split(":")
    fibonacci = [1, 1, 2, 3, 5]
    hours = time[0]
    minutes = time[1] // 5
    seconds = time[2] // 5





if __name__ == '__main__':
    print(find_fibonacci())