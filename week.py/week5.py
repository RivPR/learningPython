class Players:

    def __init__(self, name, phone_number, jersey_number):
        self.__name = name
        self.__phone_number = phone_number
        self.__jersey_number = jersey_number

    def set_name(self, name):
        self.__name = name

    def set_phone_number(self, number):
        self.__phone_number = number

    def set_jersey_number(self, number):
        self.__jersey_number = number

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_jersey_number(self):
        return self.__jersey_number

    def display_data(self):
        print("Player: " + self.__name)
        print("Phone number: " + str(self.__phone_number))
        print("Jersey: " + str(self.__jersey_number))


input_exit = True
team = {}
menu = ["Display Team Roster", "Add Member", "Remove Member", "Edit Member", "Exit Program"]


def print_welcome():
    print("Welcome to the Team Manager Program! ")


def print_menu(menu):
    count = 0
    print('\n===========Main Menu===========')
    for x in menu:
        count += 1
        if count is 5:
            count = 9
        print(str(count) + ". " + x)
    user_input = input("Make a selection: ")
    return user_input


def display_team(team):
    if len(team) == 0:
        print("No players in the team, please add one.")

    else:
        for x in team.keys():
            team[x].display_data()


def add_member(team):
    new_member = input("Name of new member: ")
    new_phone_number = input("Phone number: ")
    new_jersey_number = input("Jersey number: ")
    team[new_member] = Players(new_member, new_phone_number, new_jersey_number)
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
        team[member_edit] = Players(new_name, new_pn, new_jersey)
        print(member_edit + " has been changed. New name: " + new_name)
    else:
        print("No player found on the roster with the name: " + member_edit)
    return team


def user_selection(user_input):
    if user_input is "1":
        display_team(team)
    elif user_input is "2":
        add_member(team)
    elif user_input is "3":
        delete_member(team)
    elif user_input is "4":
        edit_member(team)
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