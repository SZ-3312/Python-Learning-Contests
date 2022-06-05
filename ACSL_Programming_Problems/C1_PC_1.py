# First programming challenge completed!
from Recurseve_functions import f, c

def card_game(values):
    score = values[0]
    index = 4

    player_hand = [values[1], values[2], values[3]]
    for i in range(4):
        if score <= 99:
            p_card = player_hand[0]
            player_hand.append(values[index])
            player_hand.remove(player_hand[0])
            p_card = calculate(p_card, score)

            score += p_card
            p_score = score
            index += 1

            if index <= 10:
                o_card = values[index]
                o_card = calculate(o_card, score)
                score += o_card
                o_score = score


                if o_score > 99 >= p_score:
                    winner = "player"
                else:
                    winner = "dealer"

        index += 1
    print(f"{score}, {winner}")


def calculate(card, score):
    if card == 0 and score + 11 <= 99:
        return 11
    elif card == 0 and score + 11 > 99:
        return 1
    elif card == 4:
        return -10
    elif card == 9:
        return 0
    return card


if __name__ == '__main__':
    inputs = [80, 9, 7, 5, 3, 1, 8, 6, 4, 2, 0]
    card_game(inputs)







