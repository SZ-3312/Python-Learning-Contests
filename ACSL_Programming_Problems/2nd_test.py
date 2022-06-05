
alphabet = []
fib_nums = ["0", "1"]
output = []
if __name__ == "__main__":
    for i in range(97, 123):
        alphabet.append(str(i))

    for i in range(26):
        fib_nums.append(str(int(fib_nums[-1]) + int(fib_nums[-2])))

    for i in range(26):
        output.append(str(int(alphabet[i]) + int(fib_nums[i])) + chr(int(alphabet[i])))

    print(' '.join(alphabet))
    print(' '.join(fib_nums))
    print(' '.join(output))

