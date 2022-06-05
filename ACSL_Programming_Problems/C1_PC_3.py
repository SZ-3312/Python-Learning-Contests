def convert(input_values):
    for i in range(len(input_values)):
        input_values[i - 1] = str(input_values[i - 1])

    new_cards = []
    index = 0
    for i in range(len(input_values) // 2):
        new_cards.append(input_values[index] + input_values[index + 1])
        index += 2

    return new_cards


def predict(cards):
    p_card = cards[0]
    d_cards = [cards[1], cards[2], cards[3], cards[4], cards[5]]
    indexes = []
    choice = "  "
    for i in range(len(d_cards)):
        if d_cards[i - 1][1] == p_card[1]:
            indexes.append(i - 1)

    if len(indexes) > 0:
        possible_choices = []
        difference = 1
        smallest_num = 1
        for i in range(len(indexes)):
            possible_choices.append(d_cards[indexes[i - 1]])
        if len(possible_choices) == 1:
            choice = possible_choices[0]
        else:
            for i in range(len(possible_choices)):
                if int(possible_choices[i - 1][0]) - difference == int(p_card[0]) < int(possible_choices[i - 1][0]):
                    choice = possible_choices[i - 1]
                    break
                else:
                    difference += 1
                    for n in range(len(possible_choices)):
                        if int(possible_choices[n - 1][0]) == smallest_num:
                            choice = possible_choices[n - 1]
                            break
                    smallest_num += 1

        print(f"{choice[0]},{choice[1]}")

    else:
        print("NONE")

# input #1: 4, "S", 2, "S", 5, "S", 6, "S", 8, "S", 9, "S" output: 5, S
# input #2: 7, "H", 3, "S", 3, "H", 3, "D", 3, "C", 2, "H" output: 2, H
# input #3: 9, "D", 3, "C", 5, "H", 1, "S", 7, "D", 9, "S" output: 7, D
# input #4: 6, "C", 1, "S", 2, "H", 7, "S", 8, "D", 9, "H" output: NONE
# input #5: 1, "D", 2, "S", 3, "D", 4, "S", 2, "H", 2, "C" output: 3, D


if __name__ == '__main__':
    values = [7, "H", 3, "S", 3, "H", 3, "D", 3, "C", 2, "H"]
    card_values = convert(values)
    predict(card_values)