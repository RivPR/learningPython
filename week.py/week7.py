import random

input_exit = True
menu = ["Roll dice.", "Exit Program."]


def print_welcome():
    print("Welcome to Craps! ")


def print_menu(menu):
    count = 0
    print('\n===========Main Menu===========')
    for x in menu:
        count += 1
        if count is 2:
            count = 9
        print(str(count) + ". " + x)
    user_input = input("Make a selection: ")
    return user_input


def roll_dice():
    die = random.randint(0, 9)
    print_die(die)
    print_value(die)
    return die


def print_die(dice):
    if dice is 1:
        print("|     |\n"
              "|  o  |\n"
              "|     |\n")
    elif dice is 2:
        print("|o    |\n"
              "|     |\n"
              "|    o|\n")
    elif dice is 3:
        print("|o    |\n"
              "|  o  |\n"
              "|    o|\n")
    elif dice is 4:
        print("|o   o|\n"
              "|     |\n"
              "|o   o|\n")
    elif dice is 5:
        print("|o   o|\n"
              "|  o  |\n"
              "|o   o|\n")
    elif dice is 6:
        print("|o   o|\n"
              "|o   o|\n"
              "|o   o|\n")
    elif dice is 7:
        print("|o   o|\n"
              "|o o o|\n"
              "|o   o|\n")
    elif dice is 8:
        print("|o o o|\n"
              "|o   o|\n"
              "|o o o|\n")
    elif dice is 9:
        print("|o o o|\n"
              "|o o o|\n"
              "|o o o|\n")
    elif dice is 0:
        print("|     |\n"
              "|     |\n"
              "|     |\n")


def print_value(die):
    print("Value of die: " + str(die))
    return die


def evaluate_result(user_die, opponent_die, user_input):
    if user_die < opponent_die and user_input is "1":
        print("You win!")
    elif user_die > opponent_die and user_input is "2":
        print("You win!")
    else:
        print("You lose! ")


def play_game():
    die_one = roll_dice()
    user_input = high_low()
    die_two = roll_dice()
    evaluate_result(die_one, die_two, user_input)


def high_low():
    print("Will your opponent get a higher or a lower number?")
    high_or_low = input("1 for higher or 2 for lower ")
    high_or_low = high_low_check(high_or_low)
    return high_or_low


def high_low_check(user_choice):
    if user_choice is "1":
        return user_choice
    elif user_choice is "2":
        return user_choice
    else:
        print("Your choice is not valid. You chose: " + str(user_choice))
        user_choice = input("Please choose 1 for your opponent to get a higher number or 2 for a lower. ")
        high_low_check(user_choice)


def user_selection(user_input):
    if user_input is "1":
        play_game()
    elif user_input is "9":
        global input_exit
        input_exit = False


def main():
    global input_exit
    global menu

    print_welcome()
    while input_exit is True:
        user_input = print_menu(menu)
        user_selection(user_input)

main()
