import random


class Winnings:
    def __init__(self, bet, total_money, jersey_number):
        self.__bet = bet
        self.__total_money = total_money
        self.__jersey_number = jersey_number

    def set_bet(self, bet):
        self.__bet = bet

    def set_total_money(self, total_money):
        self.__total_money = total_money

    def get_bet(self):
        return self.__bet

    def get_total_money(self):
        return self.__total_money

    def display_data(self):
        print("Bet: " + str(self.__bet))
        print("Current money: " + str(self.__total_money))

input_exit = True
team = {}
menu = ["Roll dice.", "Exit Program."]
winnings = {}


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
    die = random.randint(1,6)
    return die


def print_dice(dice):
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


def print_value(d1):
    print("Value of first die: " + str(d1)
          + "\nTotal: " + str(d1))
    return d1


def evaluate_result(user_die, opponent_die, user_input):
    if user_die < opponent_die and user_input is "1":
        print("You win!")
    elif user_die > opponent_die and user_input is "2":
        print("You win!")
    else:
        print("You lose! " + str(user_die) + str(opponent_die))


def play_game():
    die_one = roll_dice()
    print_dice(die_one)
    print_value(die_one)
    user_input = high_low()
    die_two = roll_dice()
    print_dice(die_two)
    print_value(die_two)
    evaluate_result(die_one, die_two, user_input)


def high_low():
    print("Will your opponent get  a higher or lower number?")
    high_or_low = input("1 for higher or 2 for lower ")
    high_low_check(high_or_low)
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


def betting(winnings):
    print("Something")


def display_team(team):
    if len(team) == 0:
        print("No players in the team, please add one.")
    else:
        for x in team.keys():
            team[x].display_data()


def add_member(winnings):
    new_member = input("Name of new member: ")
    new_phone_number = input("Phone number: ")
    new_jersey_number = input("Jersey number: ")
    team[new_member] = Winnings(new_member, new_phone_number, new_jersey_number)
    print("Member added.")
    return team


def delete_member(team):
    member_delete = input("Member to delete: ")
    if member_delete in team:
        del team[member_delete]
        print("Member deleted.")
    else:
        print(member_delete + " not found in player roster.")
    return team


def edit_member(team):
    member_edit = input("Member you want to edit: ")
    if member_edit in team:
        new_name = input("Enter the new name: ")
        new_pn = int(input("Player's phone number: "))
        new_jersey = int(input("Player's new jersey number: "))
        team[member_edit] = Winnings(new_name, new_pn, new_jersey)
        print(member_edit + " has been changed. New name: " + new_name)
    else:
        print("No player found on the roster with the name: " + member_edit)
    return team


def save_data(team):
    filename = input("Name of file to save: ")
    print("Saving data...")
    out_file = open(filename, "wt")

    for x in team.keys():
        name = str(team[x].get_name())
        phone_number = str(team[x].get_phone_number())
        jersey_number = str(team[x].get_jersey_number())
        out_file.write(str(name+","+phone_number+","+jersey_number+"\n"))
    print("Data saved.")
    out_file.close()


def load_data(team):
    file_name = input("Name of file to load: ")
    in_file = open(file_name, "rt")
    print("File loading...")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        in_line = in_line[:-1]
        name, phone_number, jersey_number = in_line.split(",")
        print(name + " " + jersey_number + " " + phone_number)
        team[name] = Winnings(name, phone_number, jersey_number)
    print("Data loaded successfully.")
    in_file.close()
    return team


def user_selection(user_input):
    if user_input is "1":
        play_game()
    elif user_input is "2":
        add_member(team)
    elif user_input is "3":
        delete_member(team)
    elif user_input is "4":
        edit_member(team)
    elif user_input is "5":
        save_data(team)
    elif user_input is "6":
        load_data(team)
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
