import fileinput
from time import time, sleep
from random import randint, choice, shuffle
from turtle import Turtle, Screen
from tkinter import messagebox
s = Screen()
t = Turtle(shape='turtle')

rare_guns = [" (Albino ", " (Buck Rogers ", " (Flame ", " (2019 "]
rare_hats = [" (Firefighter Hat)", " (Skull Bandanna)", " (Satellite Hat)", " (Astro Helmet)", " (Clan Stamp) ",
             " (Nuke Zone Pistol) ", " (Star Wars Crackshot) ", " (Staff Sash) "]
guns = ["R-PEGG)", "P-90)", "Crackshot)", "Free Ranger)", "EggK-47)", "Shotgun)", "Tri-Hard)", "Pistol)", "Grenade)"]
generated_codes = []
rare_count = 0
error_message1 = "An unexpected error occurred. (Invalid Input)"
error_message2 = "An unexpected error occurred. (Input Out of Range)"


def error_message(index):
    error = error_message1
    if index >= 1:
        error = error_message2
    messagebox.showerror("Sorry!", error)
    with open("code_bank.txt", mode="w") as data:
        data.write(error)
        data.close()
    print("No valid input was detected.")


def generate(*args):
    global rare_count
    chance = randint(0, 1000000) == 1000000
    if chr(randint(97, 123)) and randint(1, 10) in args:
        chance = True
        rare_count += 1

    new_code = []
    length = randint(9, 12)
    chars = randint(length - 2, length)

    for _ in range(chars):
        new_code.append(chr(randint(97, 122)).upper())

    for _ in range(length - chars):
        new_code.append(str(randint(0, 9)))

    shuffle(new_code)
    final_code = ''.join(new_code)
    generated_codes.append(final_code)

    if chance:
        if randint(1, 2) == 2:
            final_code += choice(rare_guns) + choice(guns)
        else:
            final_code += choice(rare_hats)

    return final_code


def write_file(codes, duration, count):
    written_output = ""
    place = 1
    for code in codes:
        written_output += f"#{place} {code}\n"
        place += 1

    written_output += f"Total Rare Codes: {count}\n"

    with open("code_bank.txt", mode="w") as data:
        data.write(written_output)
        data.write(duration)
        data.close()


def make(number):
    giveaways = 0
    epoch = time()
    while giveaways != number:
        in_progress = True
        tries = 2
        while in_progress:
            r = randint(0, 500)
            if r == 69:
                giveaways += 1
                new_code = generate(chr(randint(97, 123)), randint(1, 10))
                print(f"You won the giveaway after {tries} tries!!!\n"
                      f"Your code is: {new_code}\n"
                      f"Total giveaways attended: {giveaways}\n")

                in_progress = False

            else:
                tries += 1

    elapsed_time = f"Total time elapsed: {round(time() - epoch, 5)} seconds"
    write_file(generated_codes, elapsed_time, rare_count)
    print(elapsed_time)
    messagebox.showinfo("Progress", f"Generating Completed.\nTime Elapsed: {elapsed_time}\n"
                                    f"Total Rare Codes: {rare_count}")


if __name__ == "__main__":
    t.hideturtle()
    t.write("Getting Response...", align='center', font=('courier', 32, 'bold'))
    num_of_codes = s.textinput("Amount of Codes", "How many codes do you want to generate?\n")
    if num_of_codes == "" or 97 <= ord(num_of_codes[0]) <= 122 or " " in num_of_codes:
        error_message(0)
    elif 1 > int(num_of_codes) or int(num_of_codes) > 500000:
        error_message(1)
    else:
        estimated_time = round(int(num_of_codes)/1000 * 0.941)
        if estimated_time == 0:
            estimated_time = "Less than 1 second"
        elif estimated_time == 1:
            estimated_time = f"{str(estimated_time)} second"
        else:
            estimated_time = f"{str(estimated_time)} seconds"

        t.clear()
        t.write(f"Loading, Please wait...\n\nEstimated Time: {estimated_time}\n"
                f"\nEstimated Rare Codes: {round(int(num_of_codes)/11)}", align='center', font=('Courier', 22, 'bold'))
        make(int(num_of_codes))
        